from .hclAction import hclAction
from .common import vector4


class hclSimpleWindAction(hclAction):
    windDirection: vector4
    windMinSpeed: float
    windMaxSpeed: float
    windFrequency: float
    maximumDrag: float
    airVelocity: vector4
    currentTime: float
