"""Layer 1: Base UDTs — primitives all standards share.

Identifier, Timestamp, Quality, Value, Range, Quantity.

Tutorial:
    ts = Timestamp()
    val = Value(v=42.0, q=Quality.GOOD, t=ts, unit="degC")
"""

from dataclasses import dataclass
from enum import IntEnum
from datetime import datetime, timezone


class Quality(IntEnum):
    GOOD = 192
    UNCERTAIN = 64
    BAD = 0


@dataclass
class Identifier:
    name: str
    type: str  # UUID, PATH, TAG, URN
    scope: str
    value: str


@dataclass
class Timestamp:
    value: datetime = None

    def __post_init__(self):
        if self.value is None:
            self.value = datetime.now(timezone.utc)

    def iso(self) -> str:
        return self.value.isoformat()


@dataclass
class Value:
    v: float
    q: Quality = Quality.GOOD
    t: Timestamp = None
    unit: str | None = None

    def __post_init__(self):
        if self.t is None:
            self.t = Timestamp()


@dataclass
class Range:
    lo: float
    hi: float
    unit: str = ""
    lo_inc: bool = True
    hi_inc: bool = True

    def contains(self, v: float) -> bool:
        above = v >= self.lo if self.lo_inc else v > self.lo
        below = v <= self.hi if self.hi_inc else v < self.hi
        return above and below
