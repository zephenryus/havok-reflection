from .hkpSphereRepShape import hkpSphereRepShape
from enum import Enum


class WeldResult(Enum):
    WELD_RESULT_REJECT_CONTACT_POINT = 0
    WELD_RESULT_ACCEPT_CONTACT_POINT_MODIFIED = 1
    WELD_RESULT_ACCEPT_CONTACT_POINT_UNMODIFIED = 2


class hkpConvexShape(hkpSphereRepShape):
    radius: float
