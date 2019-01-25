from .hkpBvTreeShape import hkpBvTreeShape
from .hkpMoppCode import hkpMoppCode
from .common import any, vector4
import struct


class hkMoppBvTreeShapeBase(hkpBvTreeShape):
    code: hkpMoppCode
    moppData: any
    moppDataSize: int
    codeInfoCopy: vector4

    def __init__(self, infile):
        self.code = hkpMoppCode(infile)  # TYPE_POINTER
        self.moppData = any(infile)  # TYPE_POINTER
        self.moppDataSize = struct.unpack('>I', infile.read(4))
        self.codeInfoCopy = struct.unpack('>4f', infile.read(16))
