from .hkaiLineOfSightUtilInputBase import hkaiLineOfSightUtilInputBase
from .common import vector4


class hkaiLineOfSightUtilLineOfSightInput(hkaiLineOfSightUtilInputBase):
    goalPoint: vector4
    goalFaceKey: int
