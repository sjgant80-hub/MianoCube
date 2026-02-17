# Tutorial 7: The Konomi Standard

**Self-defining industrial standards compression**

## The Big Picture

Real factories use standards like ISA-95 (enterprise),
ISA-88 (batch control), OPC-UA (communication). The
Konomi Standard compresses ALL of them into code.

## Layer Structure

| Layer | Standard  | What It Does                   |
|-------|-----------|--------------------------------|
| 0     | Meta      | Defines how standards work     |
| 1     | Base UDTs | Shared types (ID, Time, Value) |
| 2     | ISA-95    | Enterprise ↔ control           |
| 3     | ISA-88    | Batch process states           |
| 4     | ISA-101   | HMI screen design              |
| 5     | ISA-18.2  | Alarm management               |
| 6     | OPC-UA    | Machine communication          |
| 7     | Sparkplug | MQTT pub/sub messaging         |
| 8     | Modbus    | Field device protocol          |
| 9     | KPIs      | OEE and performance metrics    |

## Quick Example

```python
from src.standard import Batch, PhaseState

batch = Batch(id="B001", recipe="vanilla")
batch.start()                    # IDLE → RUNNING
batch.transition("complete")     # RUNNING → COMPLETE
print(batch.events)              # ['Idle->Running', 'Running->Complete']
```

## Crosswalks

Standards map to each other:
- ISA-95 WorkCenter = ISA-88 ProcessCell
- OPC-UA Variable = Sparkplug Metric

See `src/standard/crosswalks.py` for the full table.
