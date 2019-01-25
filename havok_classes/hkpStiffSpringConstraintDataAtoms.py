from .hkpSetLocalTranslationsConstraintAtom import hkpSetLocalTranslationsConstraintAtom
from .hkpSetupStabilizationAtom import hkpSetupStabilizationAtom
from .hkpStiffSpringConstraintAtom import hkpStiffSpringConstraintAtom


class hkpStiffSpringConstraintDataAtoms(object):
    pivots: hkpSetLocalTranslationsConstraintAtom
    setupStabilization: hkpSetupStabilizationAtom
    spring: hkpStiffSpringConstraintAtom

    def __init__(self, infile):
        self.pivots = hkpSetLocalTranslationsConstraintAtom(infile)  # TYPE_STRUCT
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT
        self.spring = hkpStiffSpringConstraintAtom(infile)  # TYPE_STRUCT
