from .hkpSetLocalTranslationsConstraintAtom import hkpSetLocalTranslationsConstraintAtom
from .hkpSetupStabilizationAtom import hkpSetupStabilizationAtom
from .hkpStiffSpringConstraintAtom import hkpStiffSpringConstraintAtom


class hkpStiffSpringConstraintDataAtoms(object):
    pivots: hkpSetLocalTranslationsConstraintAtom
    setupStabilization: hkpSetupStabilizationAtom
    spring: hkpStiffSpringConstraintAtom

    def __init__(self, infile):
        self.pivots = hkpSetLocalTranslationsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.spring = hkpStiffSpringConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} pivots={pivots}, setupStabilization={setupStabilization}, spring={spring}>".format(**{
            "class_name": self.__class__.__name__,
            "pivots": self.pivots,
            "setupStabilization": self.setupStabilization,
            "spring": self.spring,
        })
