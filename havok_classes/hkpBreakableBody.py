from .hkReferencedObject import hkReferencedObject
from .hkpBreakableBodyController import hkpBreakableBodyController
from .hkpBreakableShape import hkpBreakableShape
import struct


class hkpBreakableBody(hkReferencedObject):
    controller: hkpBreakableBodyController
    breakableShape: hkpBreakableShape
    bodyTypeAndFlags: int
    constraintStrength: int

    def __init__(self, infile):
        self.controller = hkpBreakableBodyController(infile)  # TYPE_POINTER
        self.breakableShape = hkpBreakableShape(infile)  # TYPE_POINTER
        self.bodyTypeAndFlags = struct.unpack('>B', infile.read(1))
        self.constraintStrength = struct.unpack('>h', infile.read(2))
