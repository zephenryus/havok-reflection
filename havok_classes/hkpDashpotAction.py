from .hkpBinaryAction import hkpBinaryAction
import struct


class hkpDashpotAction(hkpBinaryAction):
    point: vector4
    strength: float
    damping: float
    impulse: vector4

    def __init__(self, infile):
        self.point = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.strength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.damping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.impulse = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} point={point}, strength={strength}, damping={damping}, impulse={impulse}>".format(**{
            "class_name": self.__class__.__name__,
            "point": self.point,
            "strength": self.strength,
            "damping": self.damping,
            "impulse": self.impulse,
        })
