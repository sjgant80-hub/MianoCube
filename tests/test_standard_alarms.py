"""Dynamic ISA-18.2 alarm tests — QUALITY metric.

Parameterized across alarm priorities and state transitions.
"""

import pytest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from standard.isa18_2 import Alarm, AlarmState, AlarmPriority

PRIORITIES = [1, 2, 3, 4]
TYPES = ["HI", "HIHI", "LO", "LOLO", "DEV"]


@pytest.mark.parametrize("priority", PRIORITIES)
def test_alarm_priority_levels(priority):
    """All priority levels create valid alarms."""
    a = Alarm(tag="TK101", type="HI", priority=priority)
    assert a.priority == priority
    assert a.state == AlarmState.NORMAL


@pytest.mark.parametrize("atype", TYPES)
def test_alarm_types(atype):
    """All alarm types create valid alarms."""
    a = Alarm(tag="TK101", type=atype)
    assert a.type == atype


def test_alarm_lifecycle():
    """Full lifecycle: NORMAL → UNACK → ACKED → NORMAL."""
    a = Alarm(tag="T1", type="HI")
    assert a.state == AlarmState.NORMAL
    a.activate()
    assert a.state == AlarmState.UNACK
    a.acknowledge("operator1")
    assert a.state == AlarmState.ACKED
    assert a.ack_user == "operator1"
    a.clear()
    assert a.state == AlarmState.NORMAL


def test_clear_unacked_goes_rtn():
    """Clearing an unacked alarm goes to RTN_UNACK."""
    a = Alarm(tag="T2", type="LO")
    a.activate()
    a.clear()
    assert a.state == AlarmState.RTN_UNACK


def test_ack_only_when_unacked():
    """Acknowledge does nothing when already normal."""
    a = Alarm(tag="T3", type="HI")
    a.acknowledge("nobody")
    assert a.state == AlarmState.NORMAL
    assert a.ack_user is None
