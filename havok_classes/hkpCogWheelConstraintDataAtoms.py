from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpCogWheelConstraintAtom import hkpCogWheelConstraintAtom


class hkpCogWheelConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    cogWheels: hkpCogWheelConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.cogWheels = hkpCogWheelConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transforms={transforms}, cogWheels={cogWheels}>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
            "cogWheels": self.cogWheels,
        })
