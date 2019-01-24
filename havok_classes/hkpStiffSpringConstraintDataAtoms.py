from .hkpSetLocalTranslationsConstraintAtom import hkpSetLocalTranslationsConstraintAtom
from .hkpSetupStabilizationAtom import hkpSetupStabilizationAtom
from .hkpStiffSpringConstraintAtom import hkpStiffSpringConstraintAtom


class hkpStiffSpringConstraintDataAtoms(object):
    pivots: hkpSetLocalTranslationsConstraintAtom
    setupStabilization: hkpSetupStabilizationAtom
    spring: hkpStiffSpringConstraintAtom
