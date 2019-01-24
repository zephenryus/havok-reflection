from .hkpHeightFieldShape import hkpHeightFieldShape
from .common import vector4


class hkpPlaneShape(hkpHeightFieldShape):
    plane: vector4
    aabbCenter: vector4
    aabbHalfExtents: vector4
