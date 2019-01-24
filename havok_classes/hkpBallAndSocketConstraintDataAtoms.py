from .hkpSetLocalTranslationsConstraintAtom import hkpSetLocalTranslationsConstraintAtom
from .hkpSetupStabilizationAtom import hkpSetupStabilizationAtom
from .hkpBallSocketConstraintAtom import hkpBallSocketConstraintAtom


class hkpBallAndSocketConstraintDataAtoms(object):
    pivots: hkpSetLocalTranslationsConstraintAtom
    setupStabilization: hkpSetupStabilizationAtom
    ballSocket: hkpBallSocketConstraintAtom
