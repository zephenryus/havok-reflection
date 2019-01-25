from .hkaiVolume import hkaiVolume
from .common import any
from .hkpShape import hkpShape
from .hkGeometry import hkGeometry


class hkaiPhysics2012ShapeVolume(hkaiVolume):
    dispatcher: any
    shape: hkpShape
    shapeTransform: any
    geometry: hkGeometry

    def __init__(self, infile):
        self.dispatcher = any(infile)  # TYPE_POINTER
        self.shape = hkpShape(infile)  # TYPE_POINTER
        self.shapeTransform = any(infile)  # TYPE_TRANSFORM
        self.geometry = hkGeometry(infile)  # TYPE_STRUCT
