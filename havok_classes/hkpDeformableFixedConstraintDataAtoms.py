from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpDeformableLinConstraintAtom import hkpDeformableLinConstraintAtom
from .hkpDeformableAngConstraintAtom import hkpDeformableAngConstraintAtom


class hkpDeformableFixedConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    lin: hkpDeformableLinConstraintAtom
    ang: hkpDeformableAngConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.lin = hkpDeformableLinConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ang = hkpDeformableAngConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transforms={transforms}, lin={lin}, ang={ang}>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
            "lin": self.lin,
            "ang": self.ang,
        })
