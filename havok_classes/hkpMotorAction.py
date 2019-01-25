from .hkpUnaryAction import hkpUnaryAction
import struct


class hkpMotorAction(hkpUnaryAction):
    axis: vector4
    spinRate: float
    gain: float
    active: bool

    def __init__(self, infile):
        self.axis = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.spinRate = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.gain = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.active = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} axis={axis}, spinRate={spinRate}, gain={gain}, active={active}>".format(**{
            "class_name": self.__class__.__name__,
            "axis": self.axis,
            "spinRate": self.spinRate,
            "gain": self.gain,
            "active": self.active,
        })
