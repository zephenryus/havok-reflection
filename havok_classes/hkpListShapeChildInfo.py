from .hkpShape import hkpShape
import struct


class hkpListShapeChildInfo(object):
    shape: hkpShape
    collisionFilterInfo: int
    shapeInfo: int
    shapeSize: int
    numChildShapes: int

    def __init__(self, infile):
        self.shape = hkpShape(infile)  # TYPE_POINTER
        self.collisionFilterInfo = struct.unpack('>I', infile.read(4))
        self.shapeInfo = struct.unpack('>H', infile.read(2))
        self.shapeSize = struct.unpack('>h', infile.read(2))
        self.numChildShapes = struct.unpack('>i', infile.read(4))
