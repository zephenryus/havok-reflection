from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpTwistLimitConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    twistAxis: int
    refAxis: int
    minAngle: float
    maxAngle: float
    angularLimitsTauFactor: float
    angularLimitsDampFactor: float
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.twistAxis = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.refAxis = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.minAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angularLimitsTauFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angularLimitsDampFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} isEnabled={isEnabled}, twistAxis={twistAxis}, refAxis={refAxis}, minAngle={minAngle}, maxAngle={maxAngle}, angularLimitsTauFactor={angularLimitsTauFactor}, angularLimitsDampFactor={angularLimitsDampFactor}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "isEnabled": self.isEnabled,
            "twistAxis": self.twistAxis,
            "refAxis": self.refAxis,
            "minAngle": self.minAngle,
            "maxAngle": self.maxAngle,
            "angularLimitsTauFactor": self.angularLimitsTauFactor,
            "angularLimitsDampFactor": self.angularLimitsDampFactor,
            "padding": self.padding,
        })
