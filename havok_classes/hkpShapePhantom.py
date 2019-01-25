from .hkpPhantom import hkpPhantom
from .hkMotionState import hkMotionState


class hkpShapePhantom(hkpPhantom):
    motionState: hkMotionState

    def __init__(self, infile):
        self.motionState = hkMotionState(infile)  # TYPE_STRUCT
