from .hkReferencedObject import hkReferencedObject
from .common import vector4, any
import struct
from .hkaiAgentTraversalInfo import hkaiAgentTraversalInfo
from .hkaiNavVolumePathSearchParameters import hkaiNavVolumePathSearchParameters
from .hkaiSearchParametersSearchBuffers import hkaiSearchParametersSearchBuffers


class hkaiVolumePathfindingUtilFindPathInput(hkReferencedObject):
    startPoint: vector4
    goalPoints: any
    startCellKey: int
    goalCellKeys: any
    maxNumberOfIterations: int
    agentInfo: hkaiAgentTraversalInfo
    searchParameters: hkaiNavVolumePathSearchParameters
    searchBuffers: hkaiSearchParametersSearchBuffers

    def __init__(self, infile):
        self.startPoint = struct.unpack('>4f', infile.read(16))
        self.goalPoints = any(infile)  # TYPE_ARRAY
        self.startCellKey = struct.unpack('>I', infile.read(4))
        self.goalCellKeys = any(infile)  # TYPE_ARRAY
        self.maxNumberOfIterations = struct.unpack('>i', infile.read(4))
        self.agentInfo = hkaiAgentTraversalInfo(infile)  # TYPE_STRUCT
        self.searchParameters = hkaiNavVolumePathSearchParameters(infile)  # TYPE_STRUCT
        self.searchBuffers = hkaiSearchParametersSearchBuffers(infile)  # TYPE_STRUCT
