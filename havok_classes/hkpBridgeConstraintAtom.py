from .hkpConstraintAtom import hkpConstraintAtom
from .hkpConstraintData import hkpConstraintData
import struct


class hkpBridgeConstraintAtom(hkpConstraintAtom):
    buildJacobianFunc: any
    constraintData: any
    padding: int

    def __init__(self, infile):
        self.buildJacobianFunc = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.constraintData = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} buildJacobianFunc={buildJacobianFunc}, constraintData={constraintData}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "buildJacobianFunc": self.buildJacobianFunc,
            "constraintData": self.constraintData,
            "padding": self.padding,
        })
