from .hkReferencedObject import hkReferencedObject
import struct
from typing import List
from .common import get_array
from .hkaiAgentTraversalInfo import hkaiAgentTraversalInfo
from .hkaiNavVolumePathSearchParameters import hkaiNavVolumePathSearchParameters
from .hkaiSearchParametersSearchBuffers import hkaiSearchParametersSearchBuffers


class hkaiVolumePathfindingUtilFindPathInput(hkReferencedObject):
    startPoint: vector4
    goalPoints: List[vector4]
    startCellKey: int
    goalCellKeys: List[int]
    maxNumberOfIterations: int
    agentInfo: hkaiAgentTraversalInfo
    searchParameters: hkaiNavVolumePathSearchParameters
    searchBuffers: hkaiSearchParametersSearchBuffers

    def __init__(self, infile):
        self.startPoint = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.goalPoints = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.startCellKey = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.goalCellKeys = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.maxNumberOfIterations = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.agentInfo = hkaiAgentTraversalInfo(infile)  # TYPE_STRUCT:TYPE_VOID
        self.searchParameters = hkaiNavVolumePathSearchParameters(infile)  # TYPE_STRUCT:TYPE_VOID
        self.searchBuffers = hkaiSearchParametersSearchBuffers(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} startPoint={startPoint}, goalPoints=[{goalPoints}], startCellKey={startCellKey}, goalCellKeys=[{goalCellKeys}], maxNumberOfIterations={maxNumberOfIterations}, agentInfo={agentInfo}, searchParameters={searchParameters}, searchBuffers={searchBuffers}>".format(**{
            "class_name": self.__class__.__name__,
            "startPoint": self.startPoint,
            "goalPoints": self.goalPoints,
            "startCellKey": self.startCellKey,
            "goalCellKeys": self.goalCellKeys,
            "maxNumberOfIterations": self.maxNumberOfIterations,
            "agentInfo": self.agentInfo,
            "searchParameters": self.searchParameters,
            "searchBuffers": self.searchBuffers,
        })
