from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpCogWheelConstraintAtom import hkpCogWheelConstraintAtom


class hkpCogWheelConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    cogWheels: hkpCogWheelConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT
        self.cogWheels = hkpCogWheelConstraintAtom(infile)  # TYPE_STRUCT
