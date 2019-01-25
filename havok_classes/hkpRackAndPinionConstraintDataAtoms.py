from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpRackAndPinionConstraintAtom import hkpRackAndPinionConstraintAtom


class hkpRackAndPinionConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    rackAndPinion: hkpRackAndPinionConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT
        self.rackAndPinion = hkpRackAndPinionConstraintAtom(infile)  # TYPE_STRUCT
