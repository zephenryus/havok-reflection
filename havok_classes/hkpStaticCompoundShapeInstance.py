from .hkpShape import hkpShape
import struct


class hkpStaticCompoundShapeInstance(object):
    transform: any
    shape: any
    filterInfo: int
    childFilterInfoMask: int
    userData: int

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_QSTRANSFORM:TYPE_VOID
        self.shape = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.filterInfo = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.childFilterInfoMask = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transform={transform}, shape={shape}, filterInfo={filterInfo}, childFilterInfoMask={childFilterInfoMask}, userData={userData}>".format(**{
            "class_name": self.__class__.__name__,
            "transform": self.transform,
            "shape": self.shape,
            "filterInfo": self.filterInfo,
            "childFilterInfoMask": self.childFilterInfoMask,
            "userData": self.userData,
        })
