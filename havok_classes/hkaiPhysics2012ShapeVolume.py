from .hkaiVolume import hkaiVolume
from .hkpShape import hkpShape
from .hkGeometry import hkGeometry


class hkaiPhysics2012ShapeVolume(hkaiVolume):
    dispatcher: any
    shape: any
    shapeTransform: any
    geometry: hkGeometry

    def __init__(self, infile):
        self.dispatcher = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.shape = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.shapeTransform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.geometry = hkGeometry(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} dispatcher={dispatcher}, shape={shape}, shapeTransform={shapeTransform}, geometry={geometry}>".format(**{
            "class_name": self.__class__.__name__,
            "dispatcher": self.dispatcher,
            "shape": self.shape,
            "shapeTransform": self.shapeTransform,
            "geometry": self.geometry,
        })
