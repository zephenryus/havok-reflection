import struct


class hkpPairCollisionFilterMapPairFilterKeyOverrideType(object):
    elem: any
    numElems: int
    hashMod: int

    def __init__(self, infile):
        self.elem = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.numElems = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.hashMod = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} elem={elem}, numElems={numElems}, hashMod={hashMod}>".format(**{
            "class_name": self.__class__.__name__,
            "elem": self.elem,
            "numElems": self.numElems,
            "hashMod": self.hashMod,
        })
