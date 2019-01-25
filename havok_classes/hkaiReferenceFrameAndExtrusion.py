from enum import Enum
import struct
from .enums import UpVectorTransformMethod


class UpVectorTransformMethod(Enum):
    USE_GLOBAL_UP = 0
    USE_INSTANCE_TRANSFORM = 1
    USE_FACE_NORMAL = 2


class hkaiReferenceFrameAndExtrusion(object):
    up: vector4
    cellExtrusion: float
    silhouetteRadiusExpasion: float
    upTransformMethod: UpVectorTransformMethod

    def __init__(self, infile):
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.cellExtrusion = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.silhouetteRadiusExpasion = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.upTransformMethod = UpVectorTransformMethod(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} up={up}, cellExtrusion={cellExtrusion}, silhouetteRadiusExpasion={silhouetteRadiusExpasion}, upTransformMethod={upTransformMethod}>".format(**{
            "class_name": self.__class__.__name__,
            "up": self.up,
            "cellExtrusion": self.cellExtrusion,
            "silhouetteRadiusExpasion": self.silhouetteRadiusExpasion,
            "upTransformMethod": self.upTransformMethod,
        })
