"""Dynamic FemtoLLM tests — PERFORMANCE metric.

Parameterized across different inputs and model configs.
"""

import pytest
import asyncio
import numpy as np


TEXTS = [
    "Hello Stephen",
    "Konomi Cube",
    "",
    "A" * 100,
    "12345",
]


def test_encode_shape(femtollm):
    """Encode must return a 16-dim vector."""
    vec = femtollm.encode("test")
    assert vec.shape == (16,)


@pytest.mark.parametrize("text", TEXTS, ids=[t[:15] or "empty" for t in TEXTS])
def test_encode_various(femtollm, text):
    """Encode handles all kinds of text input."""
    vec = femtollm.encode(text)
    assert vec.shape == (16,)
    assert vec.dtype == np.float64


def test_forward_shape(femtollm):
    """Forward pass preserves dimension."""
    x = np.ones(16)
    out = femtollm.forward(x)
    assert out.shape == (16,)


def test_forward_bounded(femtollm):
    """Tanh output is always in [-1, 1]."""
    x = np.ones(16) * 100
    out = femtollm.forward(x)
    assert all(-1 <= v <= 1 for v in out)


@pytest.mark.parametrize("text", TEXTS, ids=[t[:15] or "empty" for t in TEXTS])
def test_process_async(femtollm, text):
    """Async process must return a string for any input."""
    result = asyncio.get_event_loop().run_until_complete(
        femtollm.process(text)
    )
    assert isinstance(result, str)
    assert result.startswith("[FemtoLLM:")


def test_state_tracking(femtollm):
    """State should be idle before and after process."""
    assert femtollm.state == "idle"
    asyncio.get_event_loop().run_until_complete(femtollm.process("hi"))
    assert femtollm.state == "idle"
