"""Dynamic eVGPU tests — PERFORMANCE metric.

Parameterized across all tensor ops and activation functions.
"""

import pytest
import numpy as np


OPS = ["@", "+", "*"]
ACTIVATIONS = ["relu", "sigmoid"]


@pytest.mark.parametrize("op", OPS)
def test_tensor_ops(evgpu, matrix_pair, op):
    """Every registered tensor op must produce correct shape."""
    a, b = matrix_pair
    result = evgpu.tensor(a, b, op)
    assert result.shape == (4, 4), f"Op '{op}' returned wrong shape"


def test_tensor_bad_op(evgpu, matrix_pair):
    """Unknown ops must raise ValueError."""
    a, b = matrix_pair
    with pytest.raises(ValueError, match="Unknown op"):
        evgpu.tensor(a, b, "?")


@pytest.mark.parametrize("fn", ACTIVATIONS)
def test_activations(evgpu, fn):
    """Every activation function must return same shape."""
    x = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
    result = evgpu.activate(x, fn)
    assert result.shape == x.shape


def test_relu_values(evgpu):
    """ReLU zeroes negatives, keeps positives."""
    x = np.array([-1.0, 0.0, 1.0])
    result = evgpu.activate(x, "relu")
    np.testing.assert_array_equal(result, [0.0, 0.0, 1.0])


def test_sigmoid_range(evgpu):
    """Sigmoid output must be in (0, 1)."""
    x = np.array([-100.0, 0.0, 100.0])
    result = evgpu.activate(x, "sigmoid")
    assert all(0 <= v <= 1 for v in result)
