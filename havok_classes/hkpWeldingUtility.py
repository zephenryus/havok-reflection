from enum import Enum


class WeldingType(Enum):
    WELDING_TYPE_ANTICLOCKWISE = 0
    WELDING_TYPE_CLOCKWISE = 4
    WELDING_TYPE_TWO_SIDED = 5
    WELDING_TYPE_NONE = 6


class SectorType(Enum):
    ACCEPT_0 = 1
    SNAP_0 = 0
    REJECT = 2
    SNAP_1 = 4
    ACCEPT_1 = 3


class NumAngles(Enum):
    NUM_ANGLES = 31


class hkpWeldingUtility(object):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
