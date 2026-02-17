"""Layer 3: ISA-88 — Batch Process Control.

Equipment: ProcessCell → Unit → EquipmentModule → ControlModule
Recipes: General → Site → Master → Control
Procedure: Procedure → UnitProcedure → Operation → Phase

Tutorial:
    batch = Batch(id="B001", recipe="vanilla_ice_cream")
    batch.start()
    batch.transition("complete")
"""

from dataclasses import dataclass, field
from enum import Enum


class PhaseState(Enum):
    IDLE = "Idle"
    RUNNING = "Running"
    COMPLETE = "Complete"
    HOLDING = "Holding"
    HELD = "Held"
    RESTARTING = "Restarting"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    ABORTING = "Aborting"
    ABORTED = "Aborted"


PHASE_TRANSITIONS = {
    "Idle": {"start": "Running"},
    "Running": {"complete": "Complete", "hold": "Holding", "stop": "Stopping", "abort": "Aborting"},
    "Holding": {"held": "Held"},
    "Held": {"restart": "Restarting", "abort": "Aborting"},
    "Restarting": {"running": "Running"},
    "Stopping": {"stopped": "Stopped"},
    "Aborting": {"aborted": "Aborted"},
}


@dataclass
class Batch:
    id: str
    recipe: str
    state: PhaseState = PhaseState.IDLE
    events: list[str] = field(default_factory=list)

    def start(self):
        self.transition("start")

    def transition(self, trigger: str):
        current = self.state.value
        targets = PHASE_TRANSITIONS.get(current, {})
        next_state = targets.get(trigger)
        if next_state is None:
            raise ValueError(f"No transition '{trigger}' from {current}")
        self.state = PhaseState(next_state)
        self.events.append(f"{current}->{next_state}")
