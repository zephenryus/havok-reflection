from .hkReferencedObject import hkReferencedObject
from .hclSceneDataSetupMesh import hclSceneDataSetupMesh
from .hkxMeshSection import hkxMeshSection
import struct


class hclSceneDataSetupMeshSection(hkReferencedObject):
    setupMesh: hclSceneDataSetupMesh
    meshSection: hkxMeshSection
    skinnedSection: bool

    def __init__(self, infile):
        self.setupMesh = hclSceneDataSetupMesh(infile)  # TYPE_POINTER
        self.meshSection = hkxMeshSection(infile)  # TYPE_POINTER
        self.skinnedSection = struct.unpack('>?', infile.read(1))
