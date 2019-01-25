from .common import any
from .hkpShape import hkpShape
import struct


class hkpStaticCompoundShapeInstance(object):
    transform: any
    shape: hkpShape
    filterInfo: int
    childFilterInfoMask: int
    userData: int

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_QSTRANSFORM
        self.shape = hkpShape(infile)  # TYPE_POINTER
        self.filterInfo = struct.unpack('>I', infile.read(4))
        self.childFilterInfoMask = struct.unpack('>I', infile.read(4))
        self.userData = struct.unpack('>L', infile.read(8))
