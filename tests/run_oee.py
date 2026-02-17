"""Run full Code OEE report on the MianoCube codebase.

Usage: python -m tests.run_oee

Measures:
  AVAILABILITY  — can every module import?
  PERFORMANCE   — do all classes expose their contracts?
  QUALITY       — do all pytest tests pass?

Outputs a colored OEE dashboard to the terminal.
"""

import os
import sys
import subprocess

# Paths
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')
sys.path.insert(0, SRC)
sys.path.insert(0, os.path.join(ROOT, 'tests'))

from oee import CodeOEE
from templates import ImportTestTemplate, ModuleTestTemplate


def measure_availability(oee: CodeOEE):
    """Test every module import."""
    modules = ImportTestTemplate.discover(SRC)
    for dotpath, filepath in modules:
        ok, err = ImportTestTemplate.try_import(dotpath, SRC)
        oee.record_import(dotpath, ok, err)


def measure_performance(oee: CodeOEE):
    """Test class API contracts using instances."""
    from core import eVGPU, FemtoLLM, BlockArray, Cube, KonomiSystem
    from standard.isa95 import Equipment
    from standard.isa88 import Batch
    from standard.isa18_2 import Alarm
    from standard.kpis import OEE as OEEMetric

    instances = [
        (eVGPU(cores=2), ["tensor", "activate", "OPS", "cores"]),
        (FemtoLLM(), ["encode", "forward", "process", "HIDDEN", "state"]),
        (BlockArray((3, 3, 3)), ["set", "get", "llm_at", "active_count", "dims"]),
        (Cube("t"), ["connect", "process_vertex", "neighbors", "verts", "central"]),
        (KonomiSystem(), ["create_block_array", "create_cube", "status", "evgpu"]),
        (Equipment(id="E1", name="Test"), ["activate", "fault", "state", "mode"]),
        (Batch(id="B1", recipe="test"), ["start", "transition", "state", "events"]),
        (Alarm(tag="T1", type="HI"), ["activate", "acknowledge", "clear", "state"]),
        (OEEMetric(run=100, down=0, actual=100, ideal=100, good=100, total=100),
         ["availability", "performance", "quality", "oee"]),
    ]
    for instance, attrs in instances:
        cls_name = type(instance).__name__
        for attr in attrs:
            found = hasattr(instance, attr)
            oee.record_contract(cls_name, attr, found)


def measure_quality(oee: CodeOEE):
    """Run pytest and parse results."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=no"],
        capture_output=True, text=True, cwd=ROOT,
    )
    for line in result.stdout.splitlines():
        if " PASSED" in line:
            name = line.split(" PASSED")[0].strip()
            oee.record_test(name, True)
        elif " FAILED" in line:
            name = line.split(" FAILED")[0].strip()
            oee.record_test(name, False)
        elif " ERROR" in line:
            name = line.split(" ERROR")[0].strip()
            oee.record_test(name, False)


def color(val: float) -> str:
    """ANSI color based on value."""
    if val >= 0.95:
        return "\033[92m"  # green
    if val >= 0.85:
        return "\033[93m"  # yellow
    return "\033[91m"      # red


def reset():
    return "\033[0m"


def main():
    oee = CodeOEE()

    print("\n\033[96m" + "=" * 60)
    print("  CODE OEE REPORT — MianoCube")
    print("=" * 60 + reset() + "\n")

    print("  Measuring AVAILABILITY (module imports)...")
    measure_availability(oee)

    print("  Measuring PERFORMANCE (class contracts)...")
    measure_performance(oee)

    print("  Measuring QUALITY (pytest results)...")
    measure_quality(oee)

    r = oee.report()
    print()

    # Availability
    a = r["availability"]
    c = color(a["value"])
    print(f"  AVAILABILITY  {c}{a['pct']:>7}{reset()}  "
          f"({a['modules_ok']}/{a['modules_total']} modules)  target: {a['target']}")

    # Performance
    p = r["performance"]
    c = color(p["value"])
    print(f"  PERFORMANCE   {c}{p['pct']:>7}{reset()}  "
          f"({p['contracts_ok']}/{p['contracts_total']} contracts)  target: {p['target']}")

    # Quality
    q = r["quality"]
    c = color(q["value"])
    print(f"  QUALITY       {c}{q['pct']:>7}{reset()}  "
          f"({q['tests_passed']}/{q['tests_total']} tests, {q['tests_failed']} failed)  target: {q['target']}")

    # OEE
    o = r["oee"]
    c = color(o["value"])
    print(f"\n  {'─' * 50}")
    print(f"  CODE OEE      {c}{o['pct']:>7}{reset()}  target: {o['target']}")
    print(f"  {'─' * 50}")

    # Grade
    v = o["value"]
    if v >= 0.95:
        grade = "WORLD CLASS"
    elif v >= 0.85:
        grade = "EXCELLENT"
    elif v >= 0.70:
        grade = "GOOD"
    elif v >= 0.50:
        grade = "NEEDS IMPROVEMENT"
    else:
        grade = "CRITICAL"

    gc = color(v)
    print(f"\n  Grade: {gc}{grade}{reset()}\n")

    # Failures
    failed_imports = [d for d in oee.availability_data["details"] if not d["ok"]]
    if failed_imports:
        print("  \033[91mFailed imports:\033[0m")
        for d in failed_imports:
            print(f"    - {d['module']}: {d['error']}")

    failed_contracts = [d for d in oee.performance_data["details"] if not d["found"]]
    if failed_contracts:
        print("  \033[91mMissing contracts:\033[0m")
        for d in failed_contracts:
            print(f"    - {d['class']}.{d['attr']}")

    failed_tests = [d for d in oee.quality_data["details"] if not d["passed"]]
    if failed_tests:
        print("  \033[91mFailed tests:\033[0m")
        for d in failed_tests:
            print(f"    - {d['test']}")

    print()
    return 0 if v >= 0.85 else 1


if __name__ == "__main__":
    sys.exit(main())
