from enum import Enum
from .common import vector4
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
        self.up = struct.unpack('>4f', infile.read(16))
        self.cellExtrusion = struct.unpack('>f', infile.read(4))
        self.silhouetteRadiusExpasion = struct.unpack('>f', infile.read(4))
        self.upTransformMethod = UpVectorTransformMethod(infile)  # TYPE_ENUM
