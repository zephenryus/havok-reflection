from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpLinConstraintAtom import hkpLinConstraintAtom


class hkpPointToPlaneConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    lin: hkpLinConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT
        self.lin = hkpLinConstraintAtom(infile)  # TYPE_STRUCT
