from .hkReferencedObject import hkReferencedObject
from .hkpBreakableBodyController import hkpBreakableBodyController
from .hkpBreakableShape import hkpBreakableShape
import struct


class hkpBreakableBody(hkReferencedObject):
    controller: any
    breakableShape: any
    bodyTypeAndFlags: int
    constraintStrength: int

    def __init__(self, infile):
        self.controller = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.breakableShape = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.bodyTypeAndFlags = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.constraintStrength = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID

    def __repr__(self):
        return "<{class_name} controller={controller}, breakableShape={breakableShape}, bodyTypeAndFlags={bodyTypeAndFlags}, constraintStrength={constraintStrength}>".format(**{
            "class_name": self.__class__.__name__,
            "controller": self.controller,
            "breakableShape": self.breakableShape,
            "bodyTypeAndFlags": self.bodyTypeAndFlags,
            "constraintStrength": self.constraintStrength,
        })
