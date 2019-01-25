from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpAngConstraintAtom(hkpConstraintAtom):
    constrainedAxes: int
    numConstrainedAxes: int
    padding: int

    def __init__(self, infile):
        self.constrainedAxes = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.numConstrainedAxes = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} constrainedAxes={constrainedAxes}, numConstrainedAxes={numConstrainedAxes}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "constrainedAxes": self.constrainedAxes,
            "numConstrainedAxes": self.numConstrainedAxes,
            "padding": self.padding,
        })
