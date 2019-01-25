from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpRackAndPinionConstraintAtom import hkpRackAndPinionConstraintAtom


class hkpRackAndPinionConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    rackAndPinion: hkpRackAndPinionConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.rackAndPinion = hkpRackAndPinionConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transforms={transforms}, rackAndPinion={rackAndPinion}>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
            "rackAndPinion": self.rackAndPinion,
        })
