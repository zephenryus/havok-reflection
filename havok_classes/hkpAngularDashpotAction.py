from .hkpBinaryAction import hkpBinaryAction
import struct


class hkpAngularDashpotAction(hkpBinaryAction):
    rotation: any
    strength: float
    damping: float

    def __init__(self, infile):
        self.rotation = any(infile)  # TYPE_QUATERNION:TYPE_VOID
        self.strength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.damping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rotation={rotation}, strength={strength}, damping={damping}>".format(**{
            "class_name": self.__class__.__name__,
            "rotation": self.rotation,
            "strength": self.strength,
            "damping": self.damping,
        })
