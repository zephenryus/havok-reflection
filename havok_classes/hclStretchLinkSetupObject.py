from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
from .common import vector4
import struct


class hclStretchLinkSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: hclSimulationSetupMesh
    movableParticlesSelection: hclVertexSelectionInput
    fixedParticlesSelection: hclVertexSelectionInput
    rigidFactor: hclVertexFloatInput
    stiffness: hclVertexFloatInput
    stretchDirection: vector4
    useStretchDirection: bool
    useMeshTopology: bool
    allowDynamicLinks: bool
    useTopologicalStretchDistance: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.simulationMesh = hclSimulationSetupMesh(infile)  # TYPE_POINTER
        self.movableParticlesSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.fixedParticlesSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.rigidFactor = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.stiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.stretchDirection = struct.unpack('>4f', infile.read(16))
        self.useStretchDirection = struct.unpack('>?', infile.read(1))
        self.useMeshTopology = struct.unpack('>?', infile.read(1))
        self.allowDynamicLinks = struct.unpack('>?', infile.read(1))
        self.useTopologicalStretchDistance = struct.unpack('>?', infile.read(1))
