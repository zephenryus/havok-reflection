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
