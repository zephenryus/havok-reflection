from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpLinConstraintAtom import hkpLinConstraintAtom


class hkpPointToPlaneConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    lin: hkpLinConstraintAtom
