# Tutorial 1: eVGPU

**Electronic Virtual GPU — AI on your CPU**

## The Idea

GPUs are expensive. The eVGPU lets you do tensor math
(matrix multiply, activation functions) on regular CPU
using NumPy's optimized routines.

## Key Code (`src/core/evgpu.py`)

```python
from src.core import eVGPU
import numpy as np

gpu = eVGPU(cores=4)

# Matrix multiplication
a = np.random.randn(4, 4)
b = np.random.randn(4, 4)
result = gpu.tensor(a, b, '@')

# Element-wise addition
result = gpu.tensor(a, b, '+')

# Activation functions
x = np.array([-1, 0, 1, 2])
relu_out = gpu.activate(x, 'relu')     # [0, 0, 1, 2]
sig_out = gpu.activate(x, 'sigmoid')   # [0.27, 0.5, 0.73, 0.88]
```

## What to Notice

- `OPS` dict maps symbols to NumPy functions
- `ThreadPoolExecutor` is available for parallel work
- No GPU drivers, no CUDA — just pure Python + NumPy

## Try It

Change `cores=4` to `cores=8`. Add a new op like
`'-'` for subtraction. Run it and see.
