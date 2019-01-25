from .hkReferencedObject import hkReferencedObject
from .hkaiVolumePathfindingUtilFindPathInput import hkaiVolumePathfindingUtilFindPathInput
from .hkaiVolumePathfindingUtilFindPathOutput import hkaiVolumePathfindingUtilFindPathOutput
import struct
from .common import any


class hkaiNavVolumePathRequestInfo(hkReferencedObject):
    input: hkaiVolumePathfindingUtilFindPathInput
    output: hkaiVolumePathfindingUtilFindPathOutput
    priority: int
    owner: any
    markedForDeletion: bool

    def __init__(self, infile):
        self.input = hkaiVolumePathfindingUtilFindPathInput(infile)  # TYPE_POINTER
        self.output = hkaiVolumePathfindingUtilFindPathOutput(infile)  # TYPE_POINTER
        self.priority = struct.unpack('>i', infile.read(4))
        self.owner = any(infile)  # TYPE_POINTER
        self.markedForDeletion = struct.unpack('>?', infile.read(1))
