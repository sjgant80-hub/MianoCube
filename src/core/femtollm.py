"""FemtoLLM — 16-dimension nano language model.

Specs: 16d hidden | 1 layer | 1 head | 4MB RAM | 0.1s/req

Tutorial:
    llm = FemtoLLM()
    output = await llm.process("Hello Konomi")
"""

import numpy as np


class FemtoLLM:
    """Tiny LLM that runs anywhere."""

    HIDDEN = 16  # hidden dimension size

    def __init__(self, seed: int = 42):
        rng = np.random.RandomState(seed)
        self.W = rng.randn(self.HIDDEN, self.HIDDEN) * 0.1
        self.b = np.zeros(self.HIDDEN)
        self.state = "idle"

    def encode(self, text: str) -> np.ndarray:
        """Encode text to a 16-dim vector."""
        vec = np.zeros(self.HIDDEN)
        for i, ch in enumerate(text[: self.HIDDEN]):
            vec[i] = ord(ch) / 128.0
        return vec

    def forward(self, x: np.ndarray) -> np.ndarray:
        """Single-layer forward pass."""
        return np.tanh(self.W @ x + self.b)

    async def process(self, text: str) -> str:
        """Process text through the model."""
        self.state = "processing"
        vec = self.encode(text)
        out = self.forward(vec)
        self.state = "idle"
        return f"[FemtoLLM:{text[:30]}|norm={np.linalg.norm(out):.3f}]"
