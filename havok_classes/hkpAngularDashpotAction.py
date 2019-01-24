from .hkpBinaryAction import hkpBinaryAction
from .common import any


class hkpAngularDashpotAction(hkpBinaryAction):
    rotation: any
    strength: float
    damping: float
