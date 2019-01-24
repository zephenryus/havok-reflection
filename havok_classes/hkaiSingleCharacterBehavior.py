from .hkaiBehavior import hkaiBehavior
from .hkaiCharacter import hkaiCharacter
from .enums import CallbackType
from .hkaiNavMeshPathRequestInfo import hkaiNavMeshPathRequestInfo
from .hkaiNavVolumePathRequestInfo import hkaiNavVolumePathRequestInfo
from .hkaiSingleCharacterBehaviorRequestedGoalPoint import hkaiSingleCharacterBehaviorRequestedGoalPoint


class hkaiSingleCharacterBehavior(hkaiBehavior):
    character: hkaiCharacter
    callbackType: CallbackType
    immediateNavMeshRequest: hkaiNavMeshPathRequestInfo
    immediateNavVolumeRequest: hkaiNavVolumePathRequestInfo
    requestedGoalPoints: hkaiSingleCharacterBehaviorRequestedGoalPoint
    currentGoalIndex: int
