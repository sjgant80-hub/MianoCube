"""Layer 5: ISA-18.2 — Alarm Management Lifecycle.

Priority levels P1-P4 with response times.
Alarm states: NORMAL → UNACK → ACKED → NORMAL.
Target: <6 alarms/operator/hour average.

Tutorial:
    alarm = Alarm(tag="TK101_LVL", type="HIHI", priority=1)
    alarm.activate()
    alarm.acknowledge("operator1")
"""

from dataclasses import dataclass
from enum import Enum


class AlarmPriority(Enum):
    EMERGENCY = 1  # <1 min response
    HIGH = 2       # <10 min response
    MEDIUM = 3     # <1 hr response
    LOW = 4        # within shift


class AlarmState(Enum):
    NORMAL = "Normal"
    UNACK = "Unacknowledged"
    ACKED = "Acknowledged"
    RTN_UNACK = "ReturnedUnack"
    SHELVED = "Shelved"


@dataclass
class Alarm:
    tag: str
    type: str  # HI, HIHI, LO, LOLO, DEV
    priority: int = 3
    state: AlarmState = AlarmState.NORMAL
    setpoint: float = 0.0
    deadband: float = 0.0
    message: str = ""
    ack_user: str | None = None

    def activate(self):
        self.state = AlarmState.UNACK

    def acknowledge(self, user: str):
        if self.state == AlarmState.UNACK:
            self.state = AlarmState.ACKED
            self.ack_user = user

    def clear(self):
        if self.state == AlarmState.ACKED:
            self.state = AlarmState.NORMAL
        elif self.state == AlarmState.UNACK:
            self.state = AlarmState.RTN_UNACK
