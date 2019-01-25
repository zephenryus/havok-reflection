from .common import any
import struct


class hkpPairCollisionFilterMapPairFilterKeyOverrideType(object):
    elem: any
    numElems: int
    hashMod: int

    def __init__(self, infile):
        self.elem = any(infile)  # TYPE_POINTER
        self.numElems = struct.unpack('>i', infile.read(4))
        self.hashMod = struct.unpack('>i', infile.read(4))
