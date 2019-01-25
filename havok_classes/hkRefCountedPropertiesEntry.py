from .hkReferencedObject import hkReferencedObject
import struct


class hkRefCountedPropertiesEntry(object):
    object: hkReferencedObject
    key: int
    flags: int

    def __init__(self, infile):
        self.object = hkReferencedObject(infile)  # TYPE_POINTER
        self.key = struct.unpack('>H', infile.read(2))
        self.flags = struct.unpack('>H', infile.read(2))
