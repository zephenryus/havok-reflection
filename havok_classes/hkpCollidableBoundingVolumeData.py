from .common import any


class hkpCollidableBoundingVolumeData(object):
    min: int
    expansionMin: int
    expansionShift: int
    max: int
    expansionMax: int
    padding: int
    numChildShapeAabbs: int
    capacityChildShapeAabbs: int
    childShapeAabbs: any
    childShapeKeys: any
