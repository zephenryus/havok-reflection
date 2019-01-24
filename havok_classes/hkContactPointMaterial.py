from enum import Enum
from .hkUFloat8 import hkUFloat8


class FlagEnum(Enum):
    CONTACT_IS_NEW = 1
    CONTACT_USES_SOLVER_PATH2 = 2
    CONTACT_BREAKOFF_OBJECT_ID_SMALLER = 4
    CONTACT_IS_DISABLED = 8


class hkContactPointMaterial(object):
    userData: int
    friction: hkUFloat8
    restitution: int
    maxImpulse: hkUFloat8
    flags: int
