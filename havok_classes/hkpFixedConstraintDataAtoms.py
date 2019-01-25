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
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT
        self.ballSocket = hkpBallSocketConstraintAtom(infile)  # TYPE_STRUCT
        self.ang = hkp3dAngConstraintAtom(infile)  # TYPE_STRUCT
