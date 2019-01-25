from .hkpConstraintData import hkpConstraintData
from .hkpWheelConstraintDataAtoms import hkpWheelConstraintDataAtoms
import struct


class hkpWheelConstraintData(hkpConstraintData):
    atoms: hkpWheelConstraintDataAtoms
    initialAxleInB: vector4
    initialSteeringAxisInB: vector4

    def __init__(self, infile):
        self.atoms = hkpWheelConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID
        self.initialAxleInB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.initialSteeringAxisInB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}, initialAxleInB={initialAxleInB}, initialSteeringAxisInB={initialSteeringAxisInB}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
            "initialAxleInB": self.initialAxleInB,
            "initialSteeringAxisInB": self.initialSteeringAxisInB,
        })
