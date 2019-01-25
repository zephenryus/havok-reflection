from .hkaiBehavior import hkaiBehavior
from .hkaiCharacter import hkaiCharacter
from .enums import CallbackType
from .hkaiNavMeshPathRequestInfo import hkaiNavMeshPathRequestInfo
from .hkaiNavVolumePathRequestInfo import hkaiNavVolumePathRequestInfo
from .hkaiSingleCharacterBehaviorRequestedGoalPoint import hkaiSingleCharacterBehaviorRequestedGoalPoint
import struct


class hkaiSingleCharacterBehavior(hkaiBehavior):
    character: hkaiCharacter
    callbackType: CallbackType
    immediateNavMeshRequest: hkaiNavMeshPathRequestInfo
    immediateNavVolumeRequest: hkaiNavVolumePathRequestInfo
    requestedGoalPoints: hkaiSingleCharacterBehaviorRequestedGoalPoint
    currentGoalIndex: int

    def __init__(self, infile):
        self.character = hkaiCharacter(infile)  # TYPE_POINTER
        self.callbackType = CallbackType(infile)  # TYPE_ENUM
        self.immediateNavMeshRequest = hkaiNavMeshPathRequestInfo(infile)  # TYPE_POINTER
        self.immediateNavVolumeRequest = hkaiNavVolumePathRequestInfo(infile)  # TYPE_POINTER
        self.requestedGoalPoints = hkaiSingleCharacterBehaviorRequestedGoalPoint(infile)  # TYPE_ARRAY
        self.currentGoalIndex = struct.unpack('>i', infile.read(4))
