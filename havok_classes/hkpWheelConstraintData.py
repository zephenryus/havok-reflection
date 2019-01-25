from .hkpConstraintData import hkpConstraintData
from .hkpWheelConstraintDataAtoms import hkpWheelConstraintDataAtoms
from .common import vector4
import struct


class hkpWheelConstraintData(hkpConstraintData):
    atoms: hkpWheelConstraintDataAtoms
    initialAxleInB: vector4
    initialSteeringAxisInB: vector4

    def __init__(self, infile):
        self.atoms = hkpWheelConstraintDataAtoms(infile)  # TYPE_STRUCT
        self.initialAxleInB = struct.unpack('>4f', infile.read(16))
        self.initialSteeringAxisInB = struct.unpack('>4f', infile.read(16))
