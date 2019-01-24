from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpDeformableLinConstraintAtom import hkpDeformableLinConstraintAtom
from .hkpDeformableAngConstraintAtom import hkpDeformableAngConstraintAtom


class hkpDeformableFixedConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    lin: hkpDeformableLinConstraintAtom
    ang: hkpDeformableAngConstraintAtom
