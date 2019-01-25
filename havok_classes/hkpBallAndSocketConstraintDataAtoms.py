from .hkpSetLocalTranslationsConstraintAtom import hkpSetLocalTranslationsConstraintAtom
from .hkpSetupStabilizationAtom import hkpSetupStabilizationAtom
from .hkpBallSocketConstraintAtom import hkpBallSocketConstraintAtom


class hkpBallAndSocketConstraintDataAtoms(object):
    pivots: hkpSetLocalTranslationsConstraintAtom
    setupStabilization: hkpSetupStabilizationAtom
    ballSocket: hkpBallSocketConstraintAtom

    def __init__(self, infile):
        self.pivots = hkpSetLocalTranslationsConstraintAtom(infile)  # TYPE_STRUCT
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT
        self.ballSocket = hkpBallSocketConstraintAtom(infile)  # TYPE_STRUCT
