from .hclSetupMesh import hclSetupMesh
from typing import List
from .common import get_array
from .hclStorageSetupMeshSection import hclStorageSetupMeshSection
from .hclStorageSetupMeshVertexChannel import hclStorageSetupMeshVertexChannel
from .hclStorageSetupMeshEdgeChannel import hclStorageSetupMeshEdgeChannel
from .hclStorageSetupMeshTriangleChannel import hclStorageSetupMeshTriangleChannel
from .hclStorageSetupMeshBone import hclStorageSetupMeshBone
import struct


class hclStorageSetupMesh(hclSetupMesh):
    name: str
    worldFromMesh: any
    sections: List[hclStorageSetupMeshSection]
    vertexChannels: List[hclStorageSetupMeshVertexChannel]
    edgeChannels: List[hclStorageSetupMeshEdgeChannel]
    triangleChannels: List[hclStorageSetupMeshTriangleChannel]
    bones: List[hclStorageSetupMeshBone]
    isSkinned: bool
    stringPool: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.worldFromMesh = any(infile)  # TYPE_MATRIX4:TYPE_VOID
        self.sections = get_array(infile, hclStorageSetupMeshSection, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.vertexChannels = get_array(infile, hclStorageSetupMeshVertexChannel, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.edgeChannels = get_array(infile, hclStorageSetupMeshEdgeChannel, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.triangleChannels = get_array(infile, hclStorageSetupMeshTriangleChannel, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.bones = get_array(infile, hclStorageSetupMeshBone, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.isSkinned = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.stringPool = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", worldFromMesh={worldFromMesh}, sections=[{sections}], vertexChannels=[{vertexChannels}], edgeChannels=[{edgeChannels}], triangleChannels=[{triangleChannels}], bones=[{bones}], isSkinned={isSkinned}, stringPool={stringPool}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "worldFromMesh": self.worldFromMesh,
            "sections": self.sections,
            "vertexChannels": self.vertexChannels,
            "edgeChannels": self.edgeChannels,
            "triangleChannels": self.triangleChannels,
            "bones": self.bones,
            "isSkinned": self.isSkinned,
            "stringPool": self.stringPool,
        })
