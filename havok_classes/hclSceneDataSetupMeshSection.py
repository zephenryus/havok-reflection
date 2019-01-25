from .hkReferencedObject import hkReferencedObject
from .hclSceneDataSetupMesh import hclSceneDataSetupMesh
from .hkxMeshSection import hkxMeshSection
import struct


class hclSceneDataSetupMeshSection(hkReferencedObject):
    setupMesh: any
    meshSection: any
    skinnedSection: bool

    def __init__(self, infile):
        self.setupMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.meshSection = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.skinnedSection = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} setupMesh={setupMesh}, meshSection={meshSection}, skinnedSection={skinnedSection}>".format(**{
            "class_name": self.__class__.__name__,
            "setupMesh": self.setupMesh,
            "meshSection": self.meshSection,
            "skinnedSection": self.skinnedSection,
        })
