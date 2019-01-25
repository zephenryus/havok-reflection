from .hkpConstraintAtom import hkpConstraintAtom
from .common import any
from .hkpConstraintData import hkpConstraintData
import struct


class hkpBridgeConstraintAtom(hkpConstraintAtom):
    buildJacobianFunc: any
    constraintData: hkpConstraintData
    padding: int

    def __init__(self, infile):
        self.buildJacobianFunc = any(infile)  # TYPE_POINTER
        self.constraintData = hkpConstraintData(infile)  # TYPE_POINTER
        self.padding = struct.unpack('>B', infile.read(1))
