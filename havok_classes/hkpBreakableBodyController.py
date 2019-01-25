from .hkReferencedObject import hkReferencedObject
import struct


class hkpBreakableBodyController(hkReferencedObject):
    breakingImpulse: float

    def __init__(self, infile):
        self.breakingImpulse = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} breakingImpulse={breakingImpulse}>".format(**{
            "class_name": self.__class__.__name__,
            "breakingImpulse": self.breakingImpulse,
        })
