# Tutorial 3: BlockArray

**A 3D compute grid with LLMs at coordinates**

## The Idea

Imagine a 3D grid. Each cell at (x, y, z) can hold
a value AND a FemtoLLM. The full spec is 1000x1000x1000
(1 billion cells). We use 10x10x10 for demos.

## Key Code (`src/core/blockarray.py`)

```python
from src.core import BlockArray

ba = BlockArray((10, 10, 10))

# Set and get values
ba.set(0, 0, 0, 1.0)
ba.set(5, 5, 5, 42.0)
print(ba.get(0, 0, 0))  # 1.0

# Get an LLM at a coordinate
llm = ba.llm_at(0, 0, 0)  # creates one if needed
print(ba.active_count)     # 2 non-zero cells
```

## What to Notice

- Uses `np.zeros()` for the grid — memory efficient
- LLMs are created lazily (only when you ask for them)
- `active_count` uses `np.count_nonzero()`

## Brain Connection

In the "Cubes Are Neurons" visualization, the BlockArray
is the spatial grid where neurons live. Each coordinate
is a potential neuron location.

## Try It

Create a `(3, 3, 3)` array. Set all 27 cells to 1.0.
How many LLMs can you create? What happens at (10, 10, 10)?
