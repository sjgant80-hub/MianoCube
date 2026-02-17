"""Layer 8: Modbus — Field Device Protocol.

Register types: Coil (RW bit), DiscreteInput (RO bit),
HoldingRegister (RW u16), InputRegister (RO u16).

Tutorial:
    reg = ModbusRegister(tag="TK101_LVL", addr=40001, data_type="FLOAT32")
    fc = FUNCTION_CODES["read_hr"]  # FC03
"""

from dataclasses import dataclass
from enum import Enum


class RegisterType(Enum):
    COIL = "Coil"               # FC01/05/15
    DISCRETE_INPUT = "DI"       # FC02
    HOLDING_REG = "HR"          # FC03/06/16
    INPUT_REG = "IR"            # FC04


FUNCTION_CODES = {
    "read_coils": 1,
    "read_di": 2,
    "read_hr": 3,
    "read_ir": 4,
    "write_coil": 5,
    "write_hr": 6,
    "write_multi_coil": 15,
    "write_multi_hr": 16,
}

EXCEPTION_CODES = {
    1: "Illegal Function",
    2: "Illegal Address",
    3: "Illegal Value",
    4: "Device Failure",
}


@dataclass
class ModbusRegister:
    tag: str
    addr: int
    reg_type: RegisterType = RegisterType.HOLDING_REG
    data_type: str = "UINT16"
    scale: float = 1.0
    offset: float = 0.0
    byte_order: str = "ABCD"

    def scaled_value(self, raw: int) -> float:
        return raw * self.scale + self.offset
