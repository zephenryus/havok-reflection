from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpLinLimitConstraintAtom(hkpConstraintAtom):
    axisIndex: int
    min: float
    max: float
    padding: int

    def __init__(self, infile):
        self.axisIndex = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.min = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.max = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} axisIndex={axisIndex}, min={min}, max={max}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "axisIndex": self.axisIndex,
            "min": self.min,
            "max": self.max,
            "padding": self.padding,
        })
