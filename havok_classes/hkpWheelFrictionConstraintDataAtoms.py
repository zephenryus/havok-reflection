from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpWheelFrictionConstraintAtom import hkpWheelFrictionConstraintAtom


class hkpWheelFrictionConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    friction: hkpWheelFrictionConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.friction = hkpWheelFrictionConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transforms={transforms}, friction={friction}>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
            "friction": self.friction,
        })
