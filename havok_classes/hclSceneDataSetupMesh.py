from .hclSetupMesh import hclSetupMesh
from .hkxNode import hkxNode
from .common import any
from .hkxMesh import hkxMesh
from .hkxSkinBinding import hkxSkinBinding
from .hclSceneDataSetupMeshSection import hclSceneDataSetupMeshSection


class hclSceneDataSetupMesh(hclSetupMesh):
    node: hkxNode
    worldFromMesh: any
    mesh: hkxMesh
    skinBinding: hkxSkinBinding
    vertexChannels: any
    triangleChannels: any
    edgeChannels: any
    meshBufferInterfaces: hclSceneDataSetupMeshSection

    def __init__(self, infile):
        self.node = hkxNode(infile)  # TYPE_POINTER
        self.worldFromMesh = any(infile)  # TYPE_MATRIX4
        self.mesh = hkxMesh(infile)  # TYPE_POINTER
        self.skinBinding = hkxSkinBinding(infile)  # TYPE_POINTER
        self.vertexChannels = any(infile)  # TYPE_ARRAY
        self.triangleChannels = any(infile)  # TYPE_ARRAY
        self.edgeChannels = any(infile)  # TYPE_ARRAY
        self.meshBufferInterfaces = hclSceneDataSetupMeshSection(infile)  # TYPE_ARRAY
