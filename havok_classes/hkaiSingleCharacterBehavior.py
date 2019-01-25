from .hkaiBehavior import hkaiBehavior
from .hkaiCharacter import hkaiCharacter
from .enums import CallbackType
from .hkaiNavMeshPathRequestInfo import hkaiNavMeshPathRequestInfo
from .hkaiNavVolumePathRequestInfo import hkaiNavVolumePathRequestInfo
from typing import List
from .common import get_array
from .hkaiSingleCharacterBehaviorRequestedGoalPoint import hkaiSingleCharacterBehaviorRequestedGoalPoint
import struct


class hkaiSingleCharacterBehavior(hkaiBehavior):
    character: any
    callbackType: CallbackType
    immediateNavMeshRequest: any
    immediateNavVolumeRequest: any
    requestedGoalPoints: List[hkaiSingleCharacterBehaviorRequestedGoalPoint]
    currentGoalIndex: int

    def __init__(self, infile):
        self.character = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.callbackType = CallbackType(infile)  # TYPE_ENUM:TYPE_INT32
        self.immediateNavMeshRequest = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.immediateNavVolumeRequest = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.requestedGoalPoints = get_array(infile, hkaiSingleCharacterBehaviorRequestedGoalPoint, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.currentGoalIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} character={character}, callbackType={callbackType}, immediateNavMeshRequest={immediateNavMeshRequest}, immediateNavVolumeRequest={immediateNavVolumeRequest}, requestedGoalPoints=[{requestedGoalPoints}], currentGoalIndex={currentGoalIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "character": self.character,
            "callbackType": self.callbackType,
            "immediateNavMeshRequest": self.immediateNavMeshRequest,
            "immediateNavVolumeRequest": self.immediateNavVolumeRequest,
            "requestedGoalPoints": self.requestedGoalPoints,
            "currentGoalIndex": self.currentGoalIndex,
        })
