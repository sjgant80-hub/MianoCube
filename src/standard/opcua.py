"""Layer 6: OPC-UA — Industrial Interoperability.

Node classes: Object, Variable, Method, View, DataType.
Address space with namespaces and subscriptions.

Tutorial:
    var = OPCVariable(node_id="ns=2;s=Temp1", value=72.5)
    sub = OPCSubscription(interval_ms=1000)
    sub.add_item(var)
"""

from dataclasses import dataclass, field
from enum import Enum


class NodeClass(Enum):
    OBJECT = "Object"
    VARIABLE = "Variable"
    METHOD = "Method"
    VIEW = "View"
    DATATYPE = "DataType"


class AccessLevel(Enum):
    RO = "ReadOnly"
    RW = "ReadWrite"
    WO = "WriteOnly"


@dataclass
class OPCNode:
    node_id: str
    browse_name: str = ""
    display_name: str = ""
    node_class: NodeClass = NodeClass.OBJECT
    parent: str | None = None


@dataclass
class OPCVariable(OPCNode):
    value: float = 0.0
    data_type: str = "Double"
    access: AccessLevel = AccessLevel.RO
    historizing: bool = False

    def __post_init__(self):
        self.node_class = NodeClass.VARIABLE


@dataclass
class OPCSubscription:
    interval_ms: int = 1000
    enabled: bool = True
    items: list[str] = field(default_factory=list)

    def add_item(self, var: OPCVariable):
        self.items.append(var.node_id)
