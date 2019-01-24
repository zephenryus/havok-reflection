from enum import Enum
from .common import vector4
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
