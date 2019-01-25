import struct
from .common import any


class hkpExtendedMeshShapeSubpart(object):
    typeAndFlags: int
    shapeInfo: int
    materialStriding: int
    materialIndexStriding: int
    materialIndexBase: any
    materialBase: any
    userData: int

    def __init__(self, infile):
        self.typeAndFlags = struct.unpack('>H', infile.read(2))
        self.shapeInfo = struct.unpack('>H', infile.read(2))
        self.materialStriding = struct.unpack('>h', infile.read(2))
        self.materialIndexStriding = struct.unpack('>H', infile.read(2))
        self.materialIndexBase = any(infile)  # TYPE_POINTER
        self.materialBase = any(infile)  # TYPE_POINTER
        self.userData = struct.unpack('>L', infile.read(8))
