from .hkReferencedObject import hkReferencedObject
from .hkaiNavVolume import hkaiNavVolume
from typing import List
from .common import get_array
from .hkaiNavVolumeInstanceCellInstance import hkaiNavVolumeInstanceCellInstance
from .hkaiNavVolumeEdge import hkaiNavVolumeEdge
import struct


class hkaiNavVolumeInstance(hkReferencedObject):
    originalCells: any
    originalEdges: any
    originalVolume: any
    cellMap: List[int]
    instancedCells: List[hkaiNavVolumeInstanceCellInstance]
    ownedEdges: List[hkaiNavVolumeEdge]
    sectionUid: int
    runtimeId: int
    layer: int
    translation: vector4

    def __init__(self, infile):
        self.originalCells = any(infile)  # TYPE_SIMPLEARRAY:TYPE_VOID
        self.originalEdges = any(infile)  # TYPE_SIMPLEARRAY:TYPE_VOID
        self.originalVolume = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.cellMap = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.instancedCells = get_array(infile, hkaiNavVolumeInstanceCellInstance, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.ownedEdges = get_array(infile, hkaiNavVolumeEdge, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.sectionUid = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.runtimeId = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.layer = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.translation = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} originalCells={originalCells}, originalEdges={originalEdges}, originalVolume={originalVolume}, cellMap=[{cellMap}], instancedCells=[{instancedCells}], ownedEdges=[{ownedEdges}], sectionUid={sectionUid}, runtimeId={runtimeId}, layer={layer}, translation={translation}>".format(**{
            "class_name": self.__class__.__name__,
            "originalCells": self.originalCells,
            "originalEdges": self.originalEdges,
            "originalVolume": self.originalVolume,
            "cellMap": self.cellMap,
            "instancedCells": self.instancedCells,
            "ownedEdges": self.ownedEdges,
            "sectionUid": self.sectionUid,
            "runtimeId": self.runtimeId,
            "layer": self.layer,
            "translation": self.translation,
        })
