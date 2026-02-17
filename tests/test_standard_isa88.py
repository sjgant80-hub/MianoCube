"""Dynamic ISA-88 state machine tests — QUALITY metric.

Uses the StateMachineTemplate to generate transition tests.
"""

import pytest
import sys, os

_here = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(_here, '..', 'src'))
sys.path.insert(0, _here)

from standard.isa88 import Batch, PhaseState, PHASE_TRANSITIONS
from templates import StateMachineTemplate

_tpl = StateMachineTemplate(
    transitions=PHASE_TRANSITIONS,
    make_obj=lambda: Batch(id="T", recipe="test"),
    get_state=lambda b: b.state.value,
    do_transition=lambda b, t: b.transition(t),
)

VALID = _tpl.valid_cases()
INVALID = _tpl.invalid_cases()


@pytest.mark.parametrize(
    "from_state,trigger,to_state", VALID,
    ids=[f"{f}->{t} via {tr}" for f, tr, t in VALID]
)
def test_valid_transitions(from_state, trigger, to_state):
    """Every defined transition must reach the expected state."""
    batch = Batch(id="T", recipe="test")
    batch.state = PhaseState(from_state)
    batch.transition(trigger)
    assert batch.state.value == to_state


@pytest.mark.parametrize(
    "from_state,bad_trigger", INVALID,
    ids=[f"{f}--X--{t}" for f, t in INVALID]
)
def test_invalid_transitions(from_state, bad_trigger):
    """Invalid transitions must raise ValueError."""
    batch = Batch(id="T", recipe="test")
    batch.state = PhaseState(from_state)
    with pytest.raises(ValueError, match="No transition"):
        batch.transition(bad_trigger)


def test_batch_event_logging():
    """Batch events track all transitions."""
    b = Batch(id="B1", recipe="vanilla")
    b.start()
    b.transition("complete")
    assert len(b.events) == 2
    assert "Idle->Running" in b.events[0]
