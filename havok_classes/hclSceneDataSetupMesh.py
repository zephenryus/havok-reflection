from .hclSetupMesh import hclSetupMesh
from .hkxNode import hkxNode
from .hkxMesh import hkxMesh
from .hkxSkinBinding import hkxSkinBinding
from typing import List
from .common import get_array
from .hclSceneDataSetupMeshSection import hclSceneDataSetupMeshSection


class hclSceneDataSetupMesh(hclSetupMesh):
    node: any
    worldFromMesh: any
    mesh: any
    skinBinding: any
    vertexChannels: List[int]
    triangleChannels: List[int]
    edgeChannels: List[int]
    meshBufferInterfaces: List[hclSceneDataSetupMeshSection]

    def __init__(self, infile):
        self.node = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.worldFromMesh = any(infile)  # TYPE_MATRIX4:TYPE_VOID
        self.mesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.skinBinding = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.vertexChannels = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.triangleChannels = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.edgeChannels = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.meshBufferInterfaces = get_array(infile, hclSceneDataSetupMeshSection, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} node={node}, worldFromMesh={worldFromMesh}, mesh={mesh}, skinBinding={skinBinding}, vertexChannels=[{vertexChannels}], triangleChannels=[{triangleChannels}], edgeChannels=[{edgeChannels}], meshBufferInterfaces=[{meshBufferInterfaces}]>".format(**{
            "class_name": self.__class__.__name__,
            "node": self.node,
            "worldFromMesh": self.worldFromMesh,
            "mesh": self.mesh,
            "skinBinding": self.skinBinding,
            "vertexChannels": self.vertexChannels,
            "triangleChannels": self.triangleChannels,
            "edgeChannels": self.edgeChannels,
            "meshBufferInterfaces": self.meshBufferInterfaces,
        })
