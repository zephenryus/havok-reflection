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
        self.repathDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.incompleteRepathSegments = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.searchPathLimit = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.desiredSpeedAtEnd = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.goalDistTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.userEdgeTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.repairPaths = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.setManualControlOnUserEdges = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.pullThroughInternalVertices = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} repathDistance={repathDistance}, incompleteRepathSegments={incompleteRepathSegments}, searchPathLimit={searchPathLimit}, desiredSpeedAtEnd={desiredSpeedAtEnd}, goalDistTolerance={goalDistTolerance}, userEdgeTolerance={userEdgeTolerance}, repairPaths={repairPaths}, setManualControlOnUserEdges={setManualControlOnUserEdges}, pullThroughInternalVertices={pullThroughInternalVertices}>".format(**{
            "class_name": self.__class__.__name__,
            "repathDistance": self.repathDistance,
            "incompleteRepathSegments": self.incompleteRepathSegments,
            "searchPathLimit": self.searchPathLimit,
            "desiredSpeedAtEnd": self.desiredSpeedAtEnd,
            "goalDistTolerance": self.goalDistTolerance,
            "userEdgeTolerance": self.userEdgeTolerance,
            "repairPaths": self.repairPaths,
            "setManualControlOnUserEdges": self.setManualControlOnUserEdges,
            "pullThroughInternalVertices": self.pullThroughInternalVertices,
        })
