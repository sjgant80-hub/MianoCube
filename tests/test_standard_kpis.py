"""Dynamic KPI tests — QUALITY metric.

Parameterized across different production scenarios.
"""

import pytest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from standard.kpis import OEE, MTBF, CycleTime

OEE_CASES = [
    {"run": 450, "down": 50, "actual": 900, "ideal": 1000, "good": 890, "total": 900,
     "expected_oee": 0.9 * 0.9 * (890/900)},
    {"run": 500, "down": 0, "actual": 1000, "ideal": 1000, "good": 1000, "total": 1000,
     "expected_oee": 1.0},
    {"run": 250, "down": 250, "actual": 400, "ideal": 1000, "good": 350, "total": 400,
     "expected_oee": 0.5 * 0.4 * (350/400)},
]


@pytest.mark.parametrize("case", OEE_CASES, ids=["normal", "perfect", "poor"])
def test_oee_calculation(case):
    """OEE = availability x performance x quality."""
    expected = case["expected_oee"]
    kwargs = {k: v for k, v in case.items() if k != "expected_oee"}
    oee = OEE(**kwargs)
    assert abs(oee.oee() - expected) < 0.001


def test_oee_components():
    """Individual OEE components compute correctly."""
    oee = OEE(run=450, down=50, actual=900, ideal=1000, good=890, total=900)
    assert abs(oee.availability() - 0.9) < 0.001
    assert abs(oee.performance() - 0.9) < 0.001
    assert abs(oee.quality() - 890/900) < 0.001


def test_mtbf():
    """MTBF = total_uptime / failure_count."""
    m = MTBF(total_uptime=1000, failure_count=5)
    assert m.value() == 200.0


def test_mtbf_zero_failures():
    """Zero failures means infinite MTBF."""
    m = MTBF(total_uptime=1000, failure_count=0)
    assert m.value() == float("inf")


def test_cycle_time():
    """Cycle time efficiency = ideal / actual."""
    ct = CycleTime(ideal=10.0, actual=12.0)
    assert abs(ct.efficiency() - 10/12) < 0.001
