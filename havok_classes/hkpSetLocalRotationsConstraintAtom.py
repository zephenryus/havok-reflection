from .hkpConstraintAtom import hkpConstraintAtom
from .common import any


class hkpSetLocalRotationsConstraintAtom(hkpConstraintAtom):
    rotationA: any
    rotationB: any

    def __init__(self, infile):
        self.rotationA = any(infile)  # TYPE_ROTATION
        self.rotationB = any(infile)  # TYPE_ROTATION
