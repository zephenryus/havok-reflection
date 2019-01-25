from .hclSetupMesh import hclSetupMesh
from .hclSimulationSetupMeshMapOptions import hclSimulationSetupMeshMapOptions
import struct


class hclSimulationSetupMesh(hclSetupMesh):
    originalMesh: any
    mergeOptions: hclSimulationSetupMeshMapOptions
    mergedMeshMap: any
    worldFromOriginalMesh: any
    worldFromOriginalMeshInvTranspose: any
    originalMeshSections: any
    haveWorldTransforms: bool

    def __init__(self, infile):
        self.originalMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.mergeOptions = hclSimulationSetupMeshMapOptions(infile)  # TYPE_STRUCT:TYPE_VOID
        self.mergedMeshMap = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.worldFromOriginalMesh = any(infile)  # TYPE_MATRIX4:TYPE_VOID
        self.worldFromOriginalMeshInvTranspose = any(infile)  # TYPE_MATRIX4:TYPE_VOID
        self.originalMeshSections = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.haveWorldTransforms = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} originalMesh={originalMesh}, mergeOptions={mergeOptions}, mergedMeshMap={mergedMeshMap}, worldFromOriginalMesh={worldFromOriginalMesh}, worldFromOriginalMeshInvTranspose={worldFromOriginalMeshInvTranspose}, originalMeshSections={originalMeshSections}, haveWorldTransforms={haveWorldTransforms}>".format(**{
            "class_name": self.__class__.__name__,
            "originalMesh": self.originalMesh,
            "mergeOptions": self.mergeOptions,
            "mergedMeshMap": self.mergedMeshMap,
            "worldFromOriginalMesh": self.worldFromOriginalMesh,
            "worldFromOriginalMeshInvTranspose": self.worldFromOriginalMeshInvTranspose,
            "originalMeshSections": self.originalMeshSections,
            "haveWorldTransforms": self.haveWorldTransforms,
        })
