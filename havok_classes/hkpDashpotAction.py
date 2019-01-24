from .hkpBinaryAction import hkpBinaryAction
from .common import vector4


class hkpDashpotAction(hkpBinaryAction):
    point: vector4
    strength: float
    damping: float
    impulse: vector4
