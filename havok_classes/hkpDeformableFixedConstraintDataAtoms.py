from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpDeformableLinConstraintAtom import hkpDeformableLinConstraintAtom
from .hkpDeformableAngConstraintAtom import hkpDeformableAngConstraintAtom


class hkpDeformableFixedConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    lin: hkpDeformableLinConstraintAtom
    ang: hkpDeformableAngConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT
        self.lin = hkpDeformableLinConstraintAtom(infile)  # TYPE_STRUCT
        self.ang = hkpDeformableAngConstraintAtom(infile)  # TYPE_STRUCT
