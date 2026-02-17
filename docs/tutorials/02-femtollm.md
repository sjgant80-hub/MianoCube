# Tutorial 2: FemtoLLM

**A 16-dimension nano language model**

## The Idea

FemtoLLM is the smallest possible "language model."
16 dimensions, 1 layer, 1 attention head.
Fits in 4MB RAM. Responds in 0.1 seconds.

## Key Code (`src/core/femtollm.py`)

```python
from src.core import FemtoLLM
import asyncio

llm = FemtoLLM(seed=42)

# Encode text to a 16-dim vector
vec = llm.encode("Hello Stephen")
print(vec.shape)  # (16,)

# Forward pass through the weight matrix
out = llm.forward(vec)
print(out.shape)  # (16,)

# Full async process
result = asyncio.run(llm.process("Hello Konomi"))
print(result)
```

## What to Notice

- `encode()` maps characters to floats (ord/128)
- `forward()` is just `tanh(W @ x + b)` — one layer
- `process()` is async so it works in event loops
- `state` tracks idle/processing for monitoring

## Try It

Change `HIDDEN = 16` to `HIDDEN = 32`. Does it still work?
What changes? Check the weight matrix shape.
