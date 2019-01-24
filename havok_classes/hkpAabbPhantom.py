from .hkpPhantom import hkpPhantom
from .hkAabb import hkAabb
from .common import any


class hkpAabbPhantom(hkpPhantom):
    aabb: hkAabb
    overlappingCollidables: any
    orderDirty: bool
