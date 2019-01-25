from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpLinSoftConstraintAtom(hkpConstraintAtom):
    axisIndex: int
    tau: float
    damping: float
    padding: int

    def __init__(self, infile):
        self.axisIndex = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.tau = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.damping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} axisIndex={axisIndex}, tau={tau}, damping={damping}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "axisIndex": self.axisIndex,
            "tau": self.tau,
            "damping": self.damping,
            "padding": self.padding,
        })
