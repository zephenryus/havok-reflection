from .hkReferencedObject import hkReferencedObject
from .hkaiPathfindingUtilFindPathInput import hkaiPathfindingUtilFindPathInput
from .hkaiPathfindingUtilFindPathOutput import hkaiPathfindingUtilFindPathOutput
import struct
from .common import any


class hkaiNavMeshPathRequestInfo(hkReferencedObject):
    input: hkaiPathfindingUtilFindPathInput
    output: hkaiPathfindingUtilFindPathOutput
    priority: int
    owner: any
    markedForDeletion: bool

    def __init__(self, infile):
        self.input = hkaiPathfindingUtilFindPathInput(infile)  # TYPE_POINTER
        self.output = hkaiPathfindingUtilFindPathOutput(infile)  # TYPE_POINTER
        self.priority = struct.unpack('>i', infile.read(4))
        self.owner = any(infile)  # TYPE_POINTER
        self.markedForDeletion = struct.unpack('>?', infile.read(1))
