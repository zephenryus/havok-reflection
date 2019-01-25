from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpAngConstraintAtom(hkpConstraintAtom):
    constrainedAxes: int
    numConstrainedAxes: int
    padding: int

    def __init__(self, infile):
        self.constrainedAxes = struct.unpack('>B', infile.read(1))
        self.numConstrainedAxes = struct.unpack('>B', infile.read(1))
        self.padding = struct.unpack('>B', infile.read(1))
