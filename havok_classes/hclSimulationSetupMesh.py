from .hclSetupMesh import hclSetupMesh
from .hclSimulationSetupMeshMapOptions import hclSimulationSetupMeshMapOptions
from .common import any
import struct


class hclSimulationSetupMesh(hclSetupMesh):
    originalMesh: hclSetupMesh
    mergeOptions: hclSimulationSetupMeshMapOptions
    mergedMeshMap: any
    worldFromOriginalMesh: any
    worldFromOriginalMeshInvTranspose: any
    originalMeshSections: any
    haveWorldTransforms: bool

    def __init__(self, infile):
        self.originalMesh = hclSetupMesh(infile)  # TYPE_POINTER
        self.mergeOptions = hclSimulationSetupMeshMapOptions(infile)  # TYPE_STRUCT
        self.mergedMeshMap = any(infile)  # TYPE_POINTER
        self.worldFromOriginalMesh = any(infile)  # TYPE_MATRIX4
        self.worldFromOriginalMeshInvTranspose = any(infile)  # TYPE_MATRIX4
        self.originalMeshSections = any(infile)  # TYPE_POINTER
        self.haveWorldTransforms = struct.unpack('>?', infile.read(1))
