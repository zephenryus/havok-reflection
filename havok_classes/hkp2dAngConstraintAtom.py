from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkp2dAngConstraintAtom(hkpConstraintAtom):
    freeRotationAxis: int
    padding: int

    def __init__(self, infile):
        self.freeRotationAxis = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} freeRotationAxis={freeRotationAxis}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "freeRotationAxis": self.freeRotationAxis,
            "padding": self.padding,
        })
