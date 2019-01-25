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
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT
        self.2dAng = hkp2dAngConstraintAtom(infile)  # TYPE_STRUCT
        self.ballSocket = hkpBallSocketConstraintAtom(infile)  # TYPE_STRUCT
