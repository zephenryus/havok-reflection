from .hkpPhantom import hkpPhantom
from .hkMotionState import hkMotionState


class hkpShapePhantom(hkpPhantom):
    motionState: hkMotionState

    def __init__(self, infile):
        self.motionState = hkMotionState(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} motionState={motionState}>".format(**{
            "class_name": self.__class__.__name__,
            "motionState": self.motionState,
        })
