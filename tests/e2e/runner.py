"""
Universal AI Second Brain ? Automated E2E Test Suite Runner
Provides a CLI runner with tier filtering, rich formatted reporting, and JSON report export.
"""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
import time
import unittest
from unittest.runner import TextTestResult

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(VAULT_ROOT))

from tests.e2e.test_tier1_features import (
    TestTier1MasterBrainEntrypoint,
    TestTier1GitRulesAndToolchain,
    TestTier1AgentProfilesAndConcurrency,
    TestTier1GeminiTopicsMemoryAndProjects,
    TestTier1ObsidianParamocsAndSkills,
)
from tests.e2e.test_tier2_boundaries import (
    TestTier2WikilinksAndUnicodeBoundaries,
    TestTier2SuggestedNextStepsBoundaries,
    TestTier2ConcurrencyAndLockingBoundaries,
)
from tests.e2e.test_tier3_combinations import TestTier3CrossFeatureCombinations
from tests.e2e.test_tier4_workloads import TestTier4RealWorldWorkloads
from tests.e2e.test_tier5_adversarial import (
    TestTier5ParaMocs,
    TestTier5GeminiTopicsProjectsFidelity,
    TestTier5VaultGraphHygiene,
)

TIER_MAP = {
    "1": [
        TestTier1MasterBrainEntrypoint,
        TestTier1GitRulesAndToolchain,
        TestTier1AgentProfilesAndConcurrency,
        TestTier1GeminiTopicsMemoryAndProjects,
        TestTier1ObsidianParamocsAndSkills,
    ],
    "2": [
        TestTier2WikilinksAndUnicodeBoundaries,
        TestTier2SuggestedNextStepsBoundaries,
        TestTier2ConcurrencyAndLockingBoundaries,
    ],
    "3": [
        TestTier3CrossFeatureCombinations,
    ],
    "4": [
        TestTier4RealWorldWorkloads,
    ],
    "5": [
        TestTier5ParaMocs,
        TestTier5GeminiTopicsProjectsFidelity,
        TestTier5VaultGraphHygiene,
    ],
}


class DetailedResultCollector:
    def __init__(self):
        self.records = []

    def startTest(self, test):
        self._start_time = time.time()

    def addSuccess(self, test):
        duration = time.time() - self._start_time
        self.records.append({
            "test_id": test.id(),
            "name": test._testMethodName,
            "doc": (test.shortDescription() or "").strip(),
            "status": "PASS",
            "duration_ms": round(duration * 1000, 2),
            "error": None
        })

    def addFailure(self, test, err):
        duration = time.time() - self._start_time
        self.records.append({
            "test_id": test.id(),
            "name": test._testMethodName,
            "doc": (test.shortDescription() or "").strip(),
            "status": "FAIL",
            "duration_ms": round(duration * 1000, 2),
            "error": str(err[1])
        })

    def addError(self, test, err):
        duration = time.time() - self._start_time
        self.records.append({
            "test_id": test.id(),
            "name": test._testMethodName,
            "doc": (test.shortDescription() or "").strip(),
            "status": "ERROR",
            "duration_ms": round(duration * 1000, 2),
            "error": str(err[1])
        })

    def addSkip(self, test, reason):
        self.records.append({
            "test_id": test.id(),
            "name": test._testMethodName,
            "doc": (test.shortDescription() or "").strip(),
            "status": "SKIP",
            "duration_ms": 0.0,
            "error": reason
        })


def run_e2e_suite(tier: str = "all", verbose: bool = False, json_output: str = None) -> int:
    """Executes the specified tier or entire test suite and returns exit code (0 for pass, 1 for fail)."""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    selected_tiers = list(TIER_MAP.keys()) if tier == "all" else [tier]
    
    tier_test_counts = {}
    for t in selected_tiers:
        tier_suite = unittest.TestSuite()
        for test_cls in TIER_MAP[t]:
            tier_suite.addTests(loader.loadTestsFromTestCase(test_cls))
        tier_test_counts[t] = tier_suite.countTestCases()
        suite.addTests(tier_suite)

    collector = DetailedResultCollector()
    
    # Custom test result that hooks into listener
    class CustomTextTestResult(TextTestResult):
        def startTest(self, test):
            super().startTest(test)
            collector.startTest(test)
        def addSuccess(self, test):
            super().addSuccess(test)
            collector.addSuccess(test)
        def addFailure(self, test, err):
            super().addFailure(test, err)
            collector.addFailure(test, err)
        def addError(self, test, err):
            super().addError(test, err)
            collector.addError(test, err)
        def addSkip(self, test, reason):
            super().addSkip(test, reason)
            collector.addSkip(test, reason)

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    print("=" * 80)
    print(" === UNIVERSAL AI SECOND BRAIN -- E2E TEST SUITE RUNNER ===")
    print("=" * 80)
    print(f" Target Vault:     {VAULT_ROOT}")
    print(f" Selected Tier:    {tier.upper()}")
    print(f" Total Test Cases: {suite.countTestCases()}")
    print(f" Execution Time:   {datetime.now(timezone.utc).isoformat()}")
    print("-" * 80)

    start_time = time.time()
    runner = unittest.TextTestRunner(
        resultclass=CustomTextTestResult,
        verbosity=2 if verbose else 1,
        stream=sys.stdout
    )
    result = runner.run(suite)
    total_elapsed = time.time() - start_time

    print("\n" + "=" * 80)
    print(" === TEST EXECUTION SUMMARY ===")
    print("=" * 80)

    # Per-tier breakdown
    tier_stats = {}
    for record in collector.records:
        # Determine tier from test_id
        t_num = "unknown"
        if "tier1" in record["test_id"]:
            t_num = "1"
        elif "tier2" in record["test_id"]:
            t_num = "2"
        elif "tier3" in record["test_id"]:
            t_num = "3"
        elif "tier4" in record["test_id"]:
            t_num = "4"
        elif "tier5" in record["test_id"]:
            t_num = "5"
            
        if t_num not in tier_stats:
            tier_stats[t_num] = {"PASS": 0, "FAIL": 0, "ERROR": 0, "SKIP": 0}
        tier_stats[t_num][record["status"]] += 1

    tier_names = {
        "1": "Tier 1: Feature Coverage (Core Requirements)",
        "2": "Tier 2: Boundary & Corner Cases",
        "3": "Tier 3: Cross-Feature Combinations (Pairwise)",
        "4": "Tier 4: Real-World Workload Scenarios",
        "5": "Tier 5: Adversarial MOCs & Vault Hygiene"
    }

    for t, counts in sorted(tier_stats.items()):
        name = tier_names.get(t, f"Tier {t}")
        status_flag = "PASS" if (counts["FAIL"] == 0 and counts["ERROR"] == 0) else "FAIL"
        print(f" [{status_flag:^4}] {name:<50} Pass: {counts['PASS']:<3} Fail: {counts['FAIL']:<3} Skip: {counts['SKIP']:<3}")

    print("-" * 80)
    print(f" Total Tests: {result.testsRun} | Passed: {len(collector.records) - len(result.failures) - len(result.errors) - len(result.skipped)} | Failed: {len(result.failures)} | Errors: {len(result.errors)} | Skipped: {len(result.skipped)}")
    print(f" Total Wall-Clock Time: {round(total_elapsed, 3)} seconds")
    print("-" * 80)

    if result.wasSuccessful():
        print(" [SUCCESS] VERDICT: ALL E2E TESTS PASSED (100% SUCCESS RATE)")
        print("=" * 80)
    else:
        print(" [FAILURE] VERDICT: ONE OR MORE E2E TESTS FAILED")
        print("=" * 80)

    if json_output:
        report = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "vault": str(VAULT_ROOT),
            "tier": tier,
            "total_tests": result.testsRun,
            "passed": len(collector.records) - len(result.failures) - len(result.errors) - len(result.skipped),
            "failed": len(result.failures),
            "errors": len(result.errors),
            "skipped": len(result.skipped),
            "wall_clock_seconds": round(total_elapsed, 3),
            "verdict": "PASS" if result.wasSuccessful() else "FAIL",
            "tier_breakdown": tier_stats,
            "test_details": collector.records
        }
        with open(json_output, "w", encoding="utf-8") as jf:
            json.dump(report, jf, indent=2)
        print(f" JSON test report written to: {json_output}")

    return 0 if result.wasSuccessful() else 1


def main():
    parser = argparse.ArgumentParser(description="Universal AI Second Brain E2E Test Suite Runner")
    parser.add_argument("--tier", choices=["1", "2", "3", "4", "all"], default="all", help="Test Tier to execute")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--json", type=str, default=None, help="Path to write JSON test report")
    args = parser.parse_args()

    exit_code = run_e2e_suite(tier=args.tier, verbose=args.verbose, json_output=args.json)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
