from enum import Enum
from .hkClass import hkClass
import struct
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

    def __init__(self, infile):
        self.name = str(infile)  # TYPE_CSTRING
        self.parent = hkClass(infile)  # TYPE_POINTER
        self.objectSize = struct.unpack('>i', infile.read(4))
        self.numImplementedInterfaces = struct.unpack('>i', infile.read(4))
        self.declaredEnums = hkClassEnum(infile)  # TYPE_SIMPLEARRAY
        self.declaredMembers = hkClassMember(infile)  # TYPE_SIMPLEARRAY
        self.defaults = any(infile)  # TYPE_POINTER
        self.attributes = hkCustomAttributes(infile)  # TYPE_POINTER
        self.flags = any(infile)  # TYPE_FLAGS
        self.describedVersion = struct.unpack('>i', infile.read(4))
