from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
import struct


class hclStretchLinkSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: any
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
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simulationMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.movableParticlesSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.fixedParticlesSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.rigidFactor = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.stiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.stretchDirection = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.useStretchDirection = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.useMeshTopology = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.allowDynamicLinks = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.useTopologicalStretchDistance = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", simulationMesh={simulationMesh}, movableParticlesSelection={movableParticlesSelection}, fixedParticlesSelection={fixedParticlesSelection}, rigidFactor={rigidFactor}, stiffness={stiffness}, stretchDirection={stretchDirection}, useStretchDirection={useStretchDirection}, useMeshTopology={useMeshTopology}, allowDynamicLinks={allowDynamicLinks}, useTopologicalStretchDistance={useTopologicalStretchDistance}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "simulationMesh": self.simulationMesh,
            "movableParticlesSelection": self.movableParticlesSelection,
            "fixedParticlesSelection": self.fixedParticlesSelection,
            "rigidFactor": self.rigidFactor,
            "stiffness": self.stiffness,
            "stretchDirection": self.stretchDirection,
            "useStretchDirection": self.useStretchDirection,
            "useMeshTopology": self.useMeshTopology,
            "allowDynamicLinks": self.allowDynamicLinks,
            "useTopologicalStretchDistance": self.useTopologicalStretchDistance,
        })
