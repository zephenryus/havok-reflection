from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpAngLimitConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    limitAxis: int
    cosineAxis: int
    padding2: int
    minAngle: float
    maxAngle: float
    angularLimitsTauFactor: float
    angularLimitsDampFactor: float
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.limitAxis = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.cosineAxis = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.padding2 = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.minAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angularLimitsTauFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angularLimitsDampFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} isEnabled={isEnabled}, limitAxis={limitAxis}, cosineAxis={cosineAxis}, padding2={padding2}, minAngle={minAngle}, maxAngle={maxAngle}, angularLimitsTauFactor={angularLimitsTauFactor}, angularLimitsDampFactor={angularLimitsDampFactor}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "isEnabled": self.isEnabled,
            "limitAxis": self.limitAxis,
            "cosineAxis": self.cosineAxis,
            "padding2": self.padding2,
            "minAngle": self.minAngle,
            "maxAngle": self.maxAngle,
            "angularLimitsTauFactor": self.angularLimitsTauFactor,
            "angularLimitsDampFactor": self.angularLimitsDampFactor,
            "padding": self.padding,
        })
