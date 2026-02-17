"""Layer 0: Meta-Standard — the standard that defines standards.

Every standard in the Konomi system follows this structure.

Tutorial:
    std = STD(id="ISA-95", scope="enterprise to control")
    udt = UDT(name="Equipment", fields=[...])
"""

from dataclasses import dataclass, field


@dataclass
class RULE:
    id: str
    condition: str
    action: str
    severity: str = "info"  # info|warn|error|fatal


@dataclass
class LEVEL:
    id: str
    name: str
    scope: str
    timescale: str
    systems: list[str] = field(default_factory=list)


@dataclass
class UDT:
    name: str
    base: str | None = None
    fields: list[dict] = field(default_factory=list)
    methods: list[dict] = field(default_factory=list)
    constraints: list[RULE] = field(default_factory=list)


@dataclass
class STATE_MACHINE:
    name: str
    states: list[str] = field(default_factory=list)
    initial: str = ""
    transitions: list[dict] = field(default_factory=list)


@dataclass
class STD:
    id: str
    scope: str
    udt: list[UDT] = field(default_factory=list)
    hierarchy: list[LEVEL] = field(default_factory=list)
    states: list[STATE_MACHINE] = field(default_factory=list)
    rules: list[RULE] = field(default_factory=list)
