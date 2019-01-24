from .hkpUnaryAction import hkpUnaryAction
from .common import vector4


class hkpMotorAction(hkpUnaryAction):
    axis: vector4
    spinRate: float
    gain: float
    active: bool
