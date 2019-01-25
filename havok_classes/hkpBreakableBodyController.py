from .hkReferencedObject import hkReferencedObject
import struct


class hkpBreakableBodyController(hkReferencedObject):
    breakingImpulse: float

    def __init__(self, infile):
        self.breakingImpulse = struct.unpack('>f', infile.read(4))
