from enum import Enum


class UserEdgeDirection(Enum):
    USER_EDGE_BLOCKED = 0
    USER_EDGE_A_TO_B = 1
    USER_EDGE_B_TO_A = 2
    USER_EDGE_BIDIRECTIONAL = 3


class UserEdgeSetupSpace(Enum):
    USER_EDGE_SPACE_WORLD = 0
    USER_EDGE_SPACE_LOCAL = 1


class ClearanceResetMode(Enum):
    RESET_CLEARANCE_CACHE = 0
    DONT_RESET_CLEARANCE_CACHE = 1


class hkaiUserEdgeUtils(object):
    pass
