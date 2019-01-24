from .hclShape import hclShape
from .common import vector4


class hclCapsuleShape(hclShape):
    start: vector4
    end: vector4
    dir: vector4
    radius: float
    capLenSqrdInv: float
