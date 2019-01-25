from .hkReferencedObject import hkReferencedObject
from .hclSetupMesh import hclSetupMesh
from typing import List
from .common import get_array
from .hclSetupMeshSectionTriangle import hclSetupMeshSectionTriangle
from .hclStorageSetupMeshSectionSectionVertexChannel import hclStorageSetupMeshSectionSectionVertexChannel
from .hclStorageSetupMeshSectionSectionEdgeSelectionChannel import hclStorageSetupMeshSectionSectionEdgeSelectionChannel
from .hclStorageSetupMeshSectionSectionTriangleSelectionChannel import hclStorageSetupMeshSectionSectionTriangleSelectionChannel
from .hclStorageSetupMeshSectionBoneInfluences import hclStorageSetupMeshSectionBoneInfluences


class hclStorageSetupMeshSection(hkReferencedObject):
    parentSetupMesh: any
    vertices: List[vector4]
    normals: List[vector4]
    tangents: List[vector4]
    bitangents: List[vector4]
    triangles: List[hclSetupMeshSectionTriangle]
    sectionVertexChannels: List[hclStorageSetupMeshSectionSectionVertexChannel]
    sectionEdgeChannels: List[hclStorageSetupMeshSectionSectionEdgeSelectionChannel]
    sectionTriangleChannels: List[hclStorageSetupMeshSectionSectionTriangleSelectionChannel]
    boneInfluences: List[hclStorageSetupMeshSectionBoneInfluences]
    normalIDs: List[int]

    def __init__(self, infile):
        self.parentSetupMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.vertices = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.normals = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.tangents = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.bitangents = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.triangles = get_array(infile, hclSetupMeshSectionTriangle, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.sectionVertexChannels = get_array(infile, hclStorageSetupMeshSectionSectionVertexChannel, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.sectionEdgeChannels = get_array(infile, hclStorageSetupMeshSectionSectionEdgeSelectionChannel, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.sectionTriangleChannels = get_array(infile, hclStorageSetupMeshSectionSectionTriangleSelectionChannel, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.boneInfluences = get_array(infile, hclStorageSetupMeshSectionBoneInfluences, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.normalIDs = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16

    def __repr__(self):
        return "<{class_name} parentSetupMesh={parentSetupMesh}, vertices=[{vertices}], normals=[{normals}], tangents=[{tangents}], bitangents=[{bitangents}], triangles=[{triangles}], sectionVertexChannels=[{sectionVertexChannels}], sectionEdgeChannels=[{sectionEdgeChannels}], sectionTriangleChannels=[{sectionTriangleChannels}], boneInfluences=[{boneInfluences}], normalIDs=[{normalIDs}]>".format(**{
            "class_name": self.__class__.__name__,
            "parentSetupMesh": self.parentSetupMesh,
            "vertices": self.vertices,
            "normals": self.normals,
            "tangents": self.tangents,
            "bitangents": self.bitangents,
            "triangles": self.triangles,
            "sectionVertexChannels": self.sectionVertexChannels,
            "sectionEdgeChannels": self.sectionEdgeChannels,
            "sectionTriangleChannels": self.sectionTriangleChannels,
            "boneInfluences": self.boneInfluences,
            "normalIDs": self.normalIDs,
        })
