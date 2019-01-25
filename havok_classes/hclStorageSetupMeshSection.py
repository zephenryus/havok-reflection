from .hkReferencedObject import hkReferencedObject
from .hclSetupMesh import hclSetupMesh
from .common import any
from .hclSetupMeshSectionTriangle import hclSetupMeshSectionTriangle
from .hclStorageSetupMeshSectionSectionVertexChannel import hclStorageSetupMeshSectionSectionVertexChannel
from .hclStorageSetupMeshSectionSectionEdgeSelectionChannel import hclStorageSetupMeshSectionSectionEdgeSelectionChannel
from .hclStorageSetupMeshSectionSectionTriangleSelectionChannel import hclStorageSetupMeshSectionSectionTriangleSelectionChannel
from .hclStorageSetupMeshSectionBoneInfluences import hclStorageSetupMeshSectionBoneInfluences


class hclStorageSetupMeshSection(hkReferencedObject):
    parentSetupMesh: hclSetupMesh
    vertices: any
    normals: any
    tangents: any
    bitangents: any
    triangles: hclSetupMeshSectionTriangle
    sectionVertexChannels: hclStorageSetupMeshSectionSectionVertexChannel
    sectionEdgeChannels: hclStorageSetupMeshSectionSectionEdgeSelectionChannel
    sectionTriangleChannels: hclStorageSetupMeshSectionSectionTriangleSelectionChannel
    boneInfluences: hclStorageSetupMeshSectionBoneInfluences
    normalIDs: any

    def __init__(self, infile):
        self.parentSetupMesh = hclSetupMesh(infile)  # TYPE_POINTER
        self.vertices = any(infile)  # TYPE_ARRAY
        self.normals = any(infile)  # TYPE_ARRAY
        self.tangents = any(infile)  # TYPE_ARRAY
        self.bitangents = any(infile)  # TYPE_ARRAY
        self.triangles = hclSetupMeshSectionTriangle(infile)  # TYPE_ARRAY
        self.sectionVertexChannels = hclStorageSetupMeshSectionSectionVertexChannel(infile)  # TYPE_ARRAY
        self.sectionEdgeChannels = hclStorageSetupMeshSectionSectionEdgeSelectionChannel(infile)  # TYPE_ARRAY
        self.sectionTriangleChannels = hclStorageSetupMeshSectionSectionTriangleSelectionChannel(infile)  # TYPE_ARRAY
        self.boneInfluences = hclStorageSetupMeshSectionBoneInfluences(infile)  # TYPE_ARRAY
        self.normalIDs = any(infile)  # TYPE_ARRAY
