from .hkReferencedObject import hkReferencedObject
from .common import any, vector4
from .hkaiNavVolume import hkaiNavVolume
from .hkaiNavVolumeInstanceCellInstance import hkaiNavVolumeInstanceCellInstance
from .hkaiNavVolumeEdge import hkaiNavVolumeEdge
import struct


class hkaiNavVolumeInstance(hkReferencedObject):
    originalCells: any
    originalEdges: any
    originalVolume: hkaiNavVolume
    cellMap: any
    instancedCells: hkaiNavVolumeInstanceCellInstance
    ownedEdges: hkaiNavVolumeEdge
    sectionUid: int
    runtimeId: int
    layer: int
    translation: vector4

    def __init__(self, infile):
        self.originalCells = any(infile)  # TYPE_SIMPLEARRAY
        self.originalEdges = any(infile)  # TYPE_SIMPLEARRAY
        self.originalVolume = hkaiNavVolume(infile)  # TYPE_POINTER
        self.cellMap = any(infile)  # TYPE_ARRAY
        self.instancedCells = hkaiNavVolumeInstanceCellInstance(infile)  # TYPE_ARRAY
        self.ownedEdges = hkaiNavVolumeEdge(infile)  # TYPE_ARRAY
        self.sectionUid = struct.unpack('>I', infile.read(4))
        self.runtimeId = struct.unpack('>i', infile.read(4))
        self.layer = struct.unpack('>I', infile.read(4))
        self.translation = struct.unpack('>4f', infile.read(16))
