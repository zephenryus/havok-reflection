from .hkpSetLocalTranslationsConstraintAtom import hkpSetLocalTranslationsConstraintAtom
from .hkpSetupStabilizationAtom import hkpSetupStabilizationAtom
from .hkpBallSocketConstraintAtom import hkpBallSocketConstraintAtom


class hkpBallAndSocketConstraintDataAtoms(object):
    pivots: hkpSetLocalTranslationsConstraintAtom
    setupStabilization: hkpSetupStabilizationAtom
    ballSocket: hkpBallSocketConstraintAtom

    def __init__(self, infile):
        self.pivots = hkpSetLocalTranslationsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ballSocket = hkpBallSocketConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} pivots={pivots}, setupStabilization={setupStabilization}, ballSocket={ballSocket}>".format(**{
            "class_name": self.__class__.__name__,
            "pivots": self.pivots,
            "setupStabilization": self.setupStabilization,
            "ballSocket": self.ballSocket,
        })
