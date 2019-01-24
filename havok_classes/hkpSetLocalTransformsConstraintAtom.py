from .hkpConstraintAtom import hkpConstraintAtom
from .common import any


class hkpSetLocalTransformsConstraintAtom(hkpConstraintAtom):
    transformA: any
    transformB: any
