from .hkReferencedObject import hkReferencedObject
from .hkaiVolumePathfindingUtilFindPathInput import hkaiVolumePathfindingUtilFindPathInput
from .hkaiVolumePathfindingUtilFindPathOutput import hkaiVolumePathfindingUtilFindPathOutput
from .common import any


class hkaiNavVolumePathRequestInfo(hkReferencedObject):
    input: hkaiVolumePathfindingUtilFindPathInput
    output: hkaiVolumePathfindingUtilFindPathOutput
    priority: int
    owner: any
    markedForDeletion: bool
