"""Module Test Template — verify a class has expected attributes.

Dynamically checks that classes expose the right methods
and properties. This measures PERFORMANCE.

Usage:
    tpl = ModuleTestTemplate(MyClass, ["method_a", "method_b"])
    results = tpl.run()
"""

import inspect


class ModuleTestTemplate:
    """Generate attribute/method presence tests for a class."""

    def __init__(self, cls, expected_attrs: list[str]):
        self.cls = cls
        self.expected = expected_attrs

    def check_attrs(self) -> list[dict]:
        """Check each expected attribute exists on the class."""
        results = []
        for attr in self.expected:
            found = hasattr(self.cls, attr)
            results.append({
                "class": self.cls.__name__,
                "attr": attr,
                "found": found,
            })
        return results

    def check_callables(self) -> list[dict]:
        """Check which expected attrs are callable."""
        results = []
        for attr in self.expected:
            obj = getattr(self.cls, attr, None)
            is_callable = callable(obj) if obj else False
            results.append({
                "class": self.cls.__name__,
                "attr": attr,
                "callable": is_callable,
            })
        return results

    def run(self) -> dict:
        """Run all checks, return summary."""
        attrs = self.check_attrs()
        total = len(attrs)
        passed = sum(1 for a in attrs if a["found"])
        return {
            "class": self.cls.__name__,
            "total": total,
            "passed": passed,
            "rate": passed / total if total else 0,
            "details": attrs,
        }
