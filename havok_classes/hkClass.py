from enum import Enum
from .hkClass import hkClass
import struct
from .hkClassEnum import hkClassEnum
from .hkClassMember import hkClassMember
from .hkCustomAttributes import hkCustomAttributes


class SignatureFlags(Enum):
    SIGNATURE_LOCAL = 1


class FlagValues(Enum):
    FLAGS_NONE = 0
    FLAGS_NOT_SERIALIZABLE = 1


class hkClass(object):
    name: str
    parent: any
    objectSize: int
    numImplementedInterfaces: int
    declaredEnums: any
    declaredMembers: any
    defaults: any
    attributes: any
    flags: any
    describedVersion: int

    def __init__(self, infile):
        self.name = str(infile)  # TYPE_CSTRING:TYPE_VOID
        self.parent = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.objectSize = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numImplementedInterfaces = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.declaredEnums = any(infile)  # TYPE_SIMPLEARRAY:TYPE_STRUCT
        self.declaredMembers = any(infile)  # TYPE_SIMPLEARRAY:TYPE_STRUCT
        self.defaults = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.attributes = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT32
        self.describedVersion = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", parent={parent}, objectSize={objectSize}, numImplementedInterfaces={numImplementedInterfaces}, declaredEnums={declaredEnums}, declaredMembers={declaredMembers}, defaults={defaults}, attributes={attributes}, flags={flags}, describedVersion={describedVersion}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "parent": self.parent,
            "objectSize": self.objectSize,
            "numImplementedInterfaces": self.numImplementedInterfaces,
            "declaredEnums": self.declaredEnums,
            "declaredMembers": self.declaredMembers,
            "defaults": self.defaults,
            "attributes": self.attributes,
            "flags": self.flags,
            "describedVersion": self.describedVersion,
        })
