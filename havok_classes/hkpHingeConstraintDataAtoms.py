from enum import Enum
from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpSetupStabilizationAtom import hkpSetupStabilizationAtom
from .hkp2dAngConstraintAtom import hkp2dAngConstraintAtom
from .hkpBallSocketConstraintAtom import hkpBallSocketConstraintAtom


class Axis(Enum):
    AXIS_AXLE = 0


class hkpHingeConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    setupStabilization: hkpSetupStabilizationAtom
    2dAng: hkp2dAngConstraintAtom
    ballSocket: hkpBallSocketConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.2dAng = hkp2dAngConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ballSocket = hkpBallSocketConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transforms={transforms}, setupStabilization={setupStabilization}, 2dAng={2dAng}, ballSocket={ballSocket}>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
            "setupStabilization": self.setupStabilization,
            "2dAng": self.2dAng,
            "ballSocket": self.ballSocket,
        })
