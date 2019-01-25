from .hkpUnaryAction import hkpUnaryAction
import struct


class hkpReorientAction(hkpUnaryAction):
    rotationAxis: vector4
    upAxis: vector4
    strength: float
    damping: float

    def __init__(self, infile):
        self.rotationAxis = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.upAxis = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.strength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.damping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rotationAxis={rotationAxis}, upAxis={upAxis}, strength={strength}, damping={damping}>".format(**{
            "class_name": self.__class__.__name__,
            "rotationAxis": self.rotationAxis,
            "upAxis": self.upAxis,
            "strength": self.strength,
            "damping": self.damping,
        })
