from .hkpBvTreeShape import hkpBvTreeShape
from .hkpMoppCode import hkpMoppCode
import struct


class hkMoppBvTreeShapeBase(hkpBvTreeShape):
    code: any
    moppData: any
    moppDataSize: int
    codeInfoCopy: vector4

    def __init__(self, infile):
        self.code = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.moppData = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.moppDataSize = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.codeInfoCopy = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} code={code}, moppData={moppData}, moppDataSize={moppDataSize}, codeInfoCopy={codeInfoCopy}>".format(**{
            "class_name": self.__class__.__name__,
            "code": self.code,
            "moppData": self.moppData,
            "moppDataSize": self.moppDataSize,
            "codeInfoCopy": self.codeInfoCopy,
        })
