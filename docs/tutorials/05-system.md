# Tutorial 5: KonomiSystem

**The orchestrator that wires everything together**

## The Idea

`KonomiSystem` is the top-level object. It creates and
manages eVGPUs, BlockArrays, and Cubes. This is the
entry point from the quick-start.

## Key Code (`src/core/system.py`)

```python
from src.core import KonomiSystem
import numpy as np, asyncio

K = KonomiSystem(cores=4)

# Create a block array
ba = K.create_block_array("main", (10, 10, 10))
ba.set(0, 0, 0, 1.0)

# Create a cube
cube = K.create_cube("c1")
cube.connect("NEU", "SWD")

# Use the eVGPU
a = np.random.randn(4, 4)
b = np.random.randn(4, 4)
result = K.evgpu.tensor(a, b, '@')

# Check status
print(K.status())
# {'arrays': ['main'], 'cubes': ['c1'], 'evgpu_cores': 4}
```

## What to Notice

- One eVGPU shared across the system
- Arrays and cubes stored in dicts by name/id
- `status()` gives you a quick system overview

## Try It

Create 3 block arrays and 5 cubes. Query status.
This is how the Kontainer deployment scales.
