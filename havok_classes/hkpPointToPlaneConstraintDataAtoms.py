from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpLinConstraintAtom import hkpLinConstraintAtom


class hkpPointToPlaneConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    lin: hkpLinConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.lin = hkpLinConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transforms={transforms}, lin={lin}>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
            "lin": self.lin,
        })
