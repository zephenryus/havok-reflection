from .hkpShape import hkpShape
import struct


class hkpListShapeChildInfo(object):
    shape: any
    collisionFilterInfo: int
    shapeInfo: int
    shapeSize: int
    numChildShapes: int

    def __init__(self, infile):
        self.shape = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.collisionFilterInfo = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.shapeInfo = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.shapeSize = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.numChildShapes = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} shape={shape}, collisionFilterInfo={collisionFilterInfo}, shapeInfo={shapeInfo}, shapeSize={shapeSize}, numChildShapes={numChildShapes}>".format(**{
            "class_name": self.__class__.__name__,
            "shape": self.shape,
            "collisionFilterInfo": self.collisionFilterInfo,
            "shapeInfo": self.shapeInfo,
            "shapeSize": self.shapeSize,
            "numChildShapes": self.numChildShapes,
        })
