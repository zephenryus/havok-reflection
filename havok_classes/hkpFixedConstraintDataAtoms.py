from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpSetupStabilizationAtom import hkpSetupStabilizationAtom
from .hkpBallSocketConstraintAtom import hkpBallSocketConstraintAtom
from .hkp3dAngConstraintAtom import hkp3dAngConstraintAtom


class hkpFixedConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    setupStabilization: hkpSetupStabilizationAtom
    ballSocket: hkpBallSocketConstraintAtom
    ang: hkp3dAngConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ballSocket = hkpBallSocketConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ang = hkp3dAngConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transforms={transforms}, setupStabilization={setupStabilization}, ballSocket={ballSocket}, ang={ang}>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
            "setupStabilization": self.setupStabilization,
            "ballSocket": self.ballSocket,
            "ang": self.ang,
        })
