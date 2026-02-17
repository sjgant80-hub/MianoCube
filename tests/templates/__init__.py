"""Test templates — reusable test generators.

Templates produce parameterized test cases dynamically.
Use them to test any module against a standard contract.
"""

from .module_template import ModuleTestTemplate
from .state_machine_template import StateMachineTemplate
from .import_template import ImportTestTemplate

__all__ = [
    "ModuleTestTemplate",
    "StateMachineTemplate",
    "ImportTestTemplate",
]
