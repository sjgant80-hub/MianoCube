"""Code OEE — Overall Equipment Effectiveness for source code.

Maps the industrial OEE formula to codebase health:

  AVAILABILITY  = importable modules / total modules
  PERFORMANCE   = classes with full API contracts / total classes
  QUALITY       = tests passed / tests run

  CODE OEE = Availability x Performance x Quality

Targets (same as ISA KPI targets):
  Availability >90%  |  Performance >95%  |  Quality >99%  |  OEE >85%
"""


class CodeOEE:
    """Calculate OEE metrics for the codebase."""

    def __init__(self):
        self.availability_data = {"total": 0, "ok": 0, "details": []}
        self.performance_data = {"total": 0, "ok": 0, "details": []}
        self.quality_data = {"total": 0, "passed": 0, "failed": 0, "details": []}

    # --- Availability ---

    def record_import(self, module: str, success: bool, error: str = ""):
        self.availability_data["total"] += 1
        if success:
            self.availability_data["ok"] += 1
        self.availability_data["details"].append({
            "module": module, "ok": success, "error": error,
        })

    def availability(self) -> float:
        t = self.availability_data["total"]
        return self.availability_data["ok"] / t if t else 0

    # --- Performance ---

    def record_contract(self, cls: str, attr: str, found: bool):
        self.performance_data["total"] += 1
        if found:
            self.performance_data["ok"] += 1
        self.performance_data["details"].append({
            "class": cls, "attr": attr, "found": found,
        })

    def performance(self) -> float:
        t = self.performance_data["total"]
        return self.performance_data["ok"] / t if t else 0

    # --- Quality ---

    def record_test(self, name: str, passed: bool):
        self.quality_data["total"] += 1
        if passed:
            self.quality_data["passed"] += 1
        else:
            self.quality_data["failed"] += 1
        self.quality_data["details"].append({
            "test": name, "passed": passed,
        })

    def quality(self) -> float:
        t = self.quality_data["total"]
        return self.quality_data["passed"] / t if t else 0

    # --- OEE ---

    def oee(self) -> float:
        return self.availability() * self.performance() * self.quality()

    def report(self) -> dict:
        return {
            "availability": {
                "value": self.availability(),
                "pct": f"{self.availability()*100:.1f}%",
                "modules_ok": self.availability_data["ok"],
                "modules_total": self.availability_data["total"],
                "target": ">90%",
            },
            "performance": {
                "value": self.performance(),
                "pct": f"{self.performance()*100:.1f}%",
                "contracts_ok": self.performance_data["ok"],
                "contracts_total": self.performance_data["total"],
                "target": ">95%",
            },
            "quality": {
                "value": self.quality(),
                "pct": f"{self.quality()*100:.1f}%",
                "tests_passed": self.quality_data["passed"],
                "tests_failed": self.quality_data["failed"],
                "tests_total": self.quality_data["total"],
                "target": ">99%",
            },
            "oee": {
                "value": self.oee(),
                "pct": f"{self.oee()*100:.1f}%",
                "target": ">85%",
            },
        }
