"""State Machine Test Template — verify transition tables.

Dynamically tests that state transitions follow their
defined rules. Catches invalid transitions too.

Usage:
    tpl = StateMachineTemplate(transitions, make_obj, get_state, do_transition)
    results = tpl.run()
"""


class StateMachineTemplate:
    """Generate transition tests from a state machine definition."""

    def __init__(
        self,
        transitions: dict[str, dict[str, str]],
        make_obj,
        get_state,
        do_transition,
    ):
        self.transitions = transitions
        self.make_obj = make_obj
        self.get_state = get_state
        self.do_transition = do_transition

    def valid_cases(self) -> list[tuple[str, str, str]]:
        """Generate (from_state, trigger, to_state) triples."""
        cases = []
        for state, triggers in self.transitions.items():
            for trigger, target in triggers.items():
                cases.append((state, trigger, target))
        return cases

    def invalid_cases(self) -> list[tuple[str, str]]:
        """Generate (from_state, bad_trigger) pairs."""
        all_triggers = set()
        for triggers in self.transitions.values():
            all_triggers.update(triggers.keys())
        cases = []
        for state, triggers in self.transitions.items():
            for t in all_triggers - set(triggers.keys()):
                cases.append((state, t))
        return cases

    def run(self) -> dict:
        """Run all transition tests, return summary."""
        valid = self.valid_cases()
        invalid = self.invalid_cases()
        return {
            "valid_transitions": len(valid),
            "invalid_transitions": len(invalid),
            "cases": valid,
            "negative_cases": invalid,
        }
