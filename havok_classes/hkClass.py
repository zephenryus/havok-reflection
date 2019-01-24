from enum import Enum
from .hkClass import hkClass
from .hkClassEnum import hkClassEnum
from .hkClassMember import hkClassMember
from .common import any
from .hkCustomAttributes import hkCustomAttributes


class SignatureFlags(Enum):
    SIGNATURE_LOCAL = 1


class FlagValues(Enum):
    FLAGS_NONE = 0
    FLAGS_NOT_SERIALIZABLE = 1


class hkClass(object):
    name: str
    parent: hkClass
    objectSize: int
    numImplementedInterfaces: int
    declaredEnums: hkClassEnum
    declaredMembers: hkClassMember
    defaults: any
    attributes: hkCustomAttributes
    flags: any
    describedVersion: int
