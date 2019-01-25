from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkp3dAngConstraintAtom(hkpConstraintAtom):
    padding: int

    def __init__(self, infile):
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "padding": self.padding,
        })
