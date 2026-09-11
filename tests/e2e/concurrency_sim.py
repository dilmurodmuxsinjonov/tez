"""
Concurrency & File Locking Protocol Simulation
Implements the distributed locking and atomic write specifications for multi-agent vault operations.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import time
from typing import Any, Callable, Dict, List, Optional, Tuple


@dataclass
class LockResult:
    success: bool
    lock_file: Path
    error: Optional[str] = None
    was_stale_recovered: bool = False


class ConcurrencyProtocolManager:
    """Manages multi-agent file locks and atomic two-stage writes."""

    DEFAULT_TTL_SECONDS = 300

    def __init__(self, vault_root: Path, locks_dir: Optional[Path] = None):
        self.vault_root = vault_root
        self.locks_dir = locks_dir or (vault_root / ".agents" / "locks")
        self.locks_dir.mkdir(parents=True, exist_ok=True)
        self.audit_log = self.locks_dir / "audit.log"

    def get_lock_path(self, target_rel_path: str) -> Path:
        """Computes SHA-256 hash of relative path to form lock file name."""
        norm_path = target_rel_path.replace("\\", "/").strip().lower()
        file_hash = hashlib.sha256(norm_path.encode("utf-8")).hexdigest()
        return self.locks_dir / f"{file_hash}.lock"

    def acquire_lock(
        self,
        target_rel_path: str,
        agent_name: str,
        agent_conv_id: str,
        purpose: str,
        ttl_seconds: int = DEFAULT_TTL_SECONDS,
        current_time: Optional[float] = None,
    ) -> LockResult:
        """
        Attempts to acquire a lock on a file.
        If an active lock exists, acquisition fails.
        If a stale lock exists (age > ttl_seconds), it is broken and logged.
        """
        now_ts = current_time if current_time is not None else time.time()
        now_iso = datetime.fromtimestamp(now_ts, tz=timezone.utc).isoformat()
        lock_file = self.get_lock_path(target_rel_path)
        was_stale = False

        if lock_file.exists():
            try:
                with open(lock_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                acquired_ts = data.get("acquired_timestamp", 0)
                file_ttl = data.get("ttl_seconds", self.DEFAULT_TTL_SECONDS)
                
                if (now_ts - acquired_ts) < file_ttl:
                    # Active lock collision
                    return LockResult(
                        success=False,
                        lock_file=lock_file,
                        error=f"Collision: file locked by {data.get('locked_by')} (expires in {int(file_ttl - (now_ts - acquired_ts))}s)",
                        was_stale_recovered=False
                    )
                else:
                    # Stale lock found - break it
                    self._log_audit(f"STALE_LOCK_BROKEN: {lock_file.name} for {target_rel_path}, previously held by {data.get('locked_by')}")
                    lock_file.unlink(missing_ok=True)
                    was_stale = True
            except Exception as e:
                # Corrupt lock file, break and recover
                self._log_audit(f"CORRUPT_LOCK_RECOVERED: {lock_file.name} error: {e}")
                lock_file.unlink(missing_ok=True)
                was_stale = True

        # Write new lock file
        lock_data = {
            "target_file": target_rel_path.replace("\\", "/"),
            "locked_by": agent_name,
            "agent_conv_id": agent_conv_id,
            "acquired_at": now_iso,
            "acquired_timestamp": now_ts,
            "ttl_seconds": ttl_seconds,
            "purpose": purpose
        }

        temp_lock = lock_file.with_suffix(f".tmp.{agent_name}")
        with open(temp_lock, "w", encoding="utf-8") as f:
            json.dump(lock_data, f, indent=2)
        
        # Atomic rename into place
        temp_lock.replace(lock_file)
        self._log_audit(f"LOCK_ACQUIRED: {lock_file.name} for {target_rel_path} by {agent_name}")

        return LockResult(
            success=True,
            lock_file=lock_file,
            error=None,
            was_stale_recovered=was_stale
        )

    def release_lock(self, target_rel_path: str, agent_name: str) -> bool:
        """Releases the lock file if it exists."""
        lock_file = self.get_lock_path(target_rel_path)
        if lock_file.exists():
            try:
                with open(lock_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                holder = data.get("locked_by")
                lock_file.unlink()
                self._log_audit(f"LOCK_RELEASED: {lock_file.name} by {agent_name} (holder was {holder})")
                return True
            except Exception as e:
                lock_file.unlink(missing_ok=True)
                return True
        return False

    def atomic_write(
        self,
        dest_path: Path,
        content: str,
        agent_id: str,
        validator: Optional[Callable[[str], Tuple[bool, Optional[str]]]] = None
    ) -> Tuple[bool, Optional[str]]:
        """
        Executes two-stage atomic write:
        1. Write to <dest>.tmp.<agent_id>
        2. Run validator
        3. If valid, rename to dest_path
        4. If invalid, delete temp and return error
        """
        dest_path = Path(dest_path)
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        temp_file = dest_path.with_name(f"{dest_path.name}.tmp.{agent_id}")

        try:
            with open(temp_file, "w", encoding="utf-8") as f:
                f.write(content)

            if validator:
                is_valid, err = validator(content)
                if not is_valid:
                    temp_file.unlink(missing_ok=True)
                    return False, f"Validation failed: {err}"

            # Atomic replace
            temp_file.replace(dest_path)
            return True, None
        except Exception as e:
            temp_file.unlink(missing_ok=True)
            return False, str(e)

    def _log_audit(self, message: str) -> None:
        """Appends audit event to audit.log."""
        try:
            timestamp = datetime.now(timezone.utc).isoformat()
            with open(self.audit_log, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {message}\n")
        except Exception:
            pass
