#!/usr/bin/env python3
"""
Universal AI Second Brain ? Top-Level Automated E2E Test Suite Runner
Dispatches to tests/e2e/runner.py
"""

from pathlib import Path
import sys

VAULT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(VAULT_ROOT))

from tests.e2e.runner import main

if __name__ == "__main__":
    main()
