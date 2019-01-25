from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpWheelFrictionConstraintAtom import hkpWheelFrictionConstraintAtom


class hkpWheelFrictionConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    friction: hkpWheelFrictionConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT
        self.friction = hkpWheelFrictionConstraintAtom(infile)  # TYPE_STRUCT
