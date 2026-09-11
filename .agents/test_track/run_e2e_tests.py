#!/usr/bin/env python3
"""
Test Track Runner Forwarder
Allows running E2E tests directly from .agents/test_track/run_e2e_tests.py
"""

from pathlib import Path
import sys

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(VAULT_ROOT))

from tests.e2e.runner import main

if __name__ == "__main__":
    main()
