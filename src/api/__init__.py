"""API layer — REST and WebSocket interfaces.

REST endpoints serve the BlockArray (3D grid).
WebSocket serves the Cube (9-node processor).
"""

from .rest import create_rest_app
from .websocket import create_ws_server

__all__ = ["create_rest_app", "create_ws_server"]
