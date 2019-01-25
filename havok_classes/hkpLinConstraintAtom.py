from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpLinConstraintAtom(hkpConstraintAtom):
    axisIndex: int
    padding: int

    def __init__(self, infile):
        self.axisIndex = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} axisIndex={axisIndex}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "axisIndex": self.axisIndex,
            "padding": self.padding,
        })
