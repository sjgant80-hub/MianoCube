"""Layer 7: MQTT/Sparkplug — Lightweight Pub/Sub.

Topic format: spBv1.0/{group}/{msgtype}/{edge}/{device}
Message types: NBIRTH, NDEATH, DBIRTH, DDEATH, NDATA, DDATA, NCMD, DCMD.

Tutorial:
    topic = sparkplug_topic("Plant1", "NDATA", "PLC01")
    payload = SparkplugPayload(metrics=[{"name": "Temp", "value": 72.5}])
"""

from dataclasses import dataclass, field
from enum import Enum


class QoS(Enum):
    AT_MOST_ONCE = 0
    AT_LEAST_ONCE = 1
    EXACTLY_ONCE = 2


class MsgType(Enum):
    NBIRTH = "NBIRTH"
    NDEATH = "NDEATH"
    DBIRTH = "DBIRTH"
    DDEATH = "DDEATH"
    NDATA = "NDATA"
    DDATA = "DDATA"
    NCMD = "NCMD"
    DCMD = "DCMD"


def sparkplug_topic(
    group: str, msg_type: str, edge: str, device: str = ""
) -> str:
    """Build a Sparkplug B topic string."""
    base = f"spBv1.0/{group}/{msg_type}/{edge}"
    return f"{base}/{device}" if device else base


@dataclass
class SparkplugPayload:
    metrics: list[dict] = field(default_factory=list)
    seq: int = 0

    def add_metric(self, name: str, value, datatype: str = "Double"):
        self.metrics.append({
            "name": name, "value": value, "datatype": datatype,
        })
