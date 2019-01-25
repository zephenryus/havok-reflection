from .hkpConstraintAtom import hkpConstraintAtom
from .common import any


class hkpSetLocalTransformsConstraintAtom(hkpConstraintAtom):
    transformA: any
    transformB: any

    def __init__(self, infile):
        self.transformA = any(infile)  # TYPE_TRANSFORM
        self.transformB = any(infile)  # TYPE_TRANSFORM
