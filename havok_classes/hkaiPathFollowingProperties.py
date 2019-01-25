from .hkReferencedObject import hkReferencedObject
import struct


class hkaiPathFollowingProperties(hkReferencedObject):
    repathDistance: float
    incompleteRepathSegments: int
    searchPathLimit: float
    desiredSpeedAtEnd: float
    goalDistTolerance: float
    userEdgeTolerance: float
    repairPaths: bool
    setManualControlOnUserEdges: bool
    pullThroughInternalVertices: bool

    def __init__(self, infile):
        self.repathDistance = struct.unpack('>f', infile.read(4))
        self.incompleteRepathSegments = struct.unpack('>i', infile.read(4))
        self.searchPathLimit = struct.unpack('>f', infile.read(4))
        self.desiredSpeedAtEnd = struct.unpack('>f', infile.read(4))
        self.goalDistTolerance = struct.unpack('>f', infile.read(4))
        self.userEdgeTolerance = struct.unpack('>f', infile.read(4))
        self.repairPaths = struct.unpack('>?', infile.read(1))
        self.setManualControlOnUserEdges = struct.unpack('>?', infile.read(1))
        self.pullThroughInternalVertices = struct.unpack('>?', infile.read(1))
