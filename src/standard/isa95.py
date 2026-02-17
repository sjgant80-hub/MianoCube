"""Layer 2: ISA-95 — Enterprise to Control Integration.

Levels: L4 Business → L3 MOM → L2 Control → L1 Sensing → L0 Process
Hierarchy: Enterprise → Site → Area → WorkCenter → WorkUnit → Equipment

Tutorial:
    site = Equipment(id="S1", name="Plant Alpha", level=ISA95Level.L4)
"""

from dataclasses import dataclass, field
from enum import Enum


class ISA95Level(Enum):
    L0 = "Process"
    L1 = "Sensing"
    L2 = "Control"
    L3 = "MOM"
    L4 = "Business"


class EquipmentState(Enum):
    IDLE = "Idle"
    RUNNING = "Running"
    FAULTED = "Faulted"
    MAINTENANCE = "Maintenance"
    OFFLINE = "Offline"


class EquipmentMode(Enum):
    PRODUCTION = "Production"
    MAINTENANCE = "Maintenance"
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"


@dataclass
class Equipment:
    id: str
    name: str
    level: ISA95Level = ISA95Level.L0
    state: EquipmentState = EquipmentState.IDLE
    mode: EquipmentMode = EquipmentMode.AUTOMATIC
    parent: str | None = None
    children: list[str] = field(default_factory=list)

    def activate(self):
        self.state = EquipmentState.RUNNING

    def fault(self):
        self.state = EquipmentState.FAULTED


@dataclass
class ProcessSegment:
    id: str
    name: str
    equipment: list[str] = field(default_factory=list)
    params: dict = field(default_factory=dict)
