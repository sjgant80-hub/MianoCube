"""Layer 9: KPIs — Operational Performance Metrics.

OEE = Availability x Performance x Quality.
Target: Availability >90%, Performance >95%, Quality >99%, OEE >85%.

Tutorial:
    oee = OEE(run=450, down=50, actual=900, ideal=1000, good=890, total=900)
    print(oee.oee())  # 0.801
"""

from dataclasses import dataclass


@dataclass
class OEE:
    """Overall Equipment Effectiveness."""
    run: float       # run time (minutes)
    down: float      # downtime (minutes)
    actual: float    # actual units produced
    ideal: float     # ideal units in same time
    good: float      # good units
    total: float     # total units attempted

    def availability(self) -> float:
        return self.run / (self.run + self.down)

    def performance(self) -> float:
        return self.actual / self.ideal if self.ideal else 0

    def quality(self) -> float:
        return self.good / self.total if self.total else 0

    def oee(self) -> float:
        return self.availability() * self.performance() * self.quality()


@dataclass
class MTBF:
    """Mean Time Between Failures."""
    total_uptime: float
    failure_count: int

    def value(self) -> float:
        return self.total_uptime / self.failure_count if self.failure_count else float("inf")


@dataclass
class CycleTime:
    """Cycle time tracking."""
    ideal: float
    actual: float

    def efficiency(self) -> float:
        return self.ideal / self.actual if self.actual else 0
