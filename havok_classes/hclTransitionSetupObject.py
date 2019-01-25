from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
import struct
from .hclBufferSetupObject import hclBufferSetupObject


class hclTransitionSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: any
    vertexSelection: hclVertexSelectionInput
    toAnimDelay: hclVertexFloatInput
    toSimDelay: hclVertexFloatInput
    toSimMaxDistance: hclVertexFloatInput
    toAnimPeriod: float
    toSimPeriod: float
    referenceBufferSetup: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simulationMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.toAnimDelay = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.toSimDelay = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.toSimMaxDistance = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.toAnimPeriod = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.toSimPeriod = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.referenceBufferSetup = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} name=\"{name}\", simulationMesh={simulationMesh}, vertexSelection={vertexSelection}, toAnimDelay={toAnimDelay}, toSimDelay={toSimDelay}, toSimMaxDistance={toSimMaxDistance}, toAnimPeriod={toAnimPeriod}, toSimPeriod={toSimPeriod}, referenceBufferSetup={referenceBufferSetup}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "simulationMesh": self.simulationMesh,
            "vertexSelection": self.vertexSelection,
            "toAnimDelay": self.toAnimDelay,
            "toSimDelay": self.toSimDelay,
            "toSimMaxDistance": self.toSimMaxDistance,
            "toAnimPeriod": self.toAnimPeriod,
            "toSimPeriod": self.toSimPeriod,
            "referenceBufferSetup": self.referenceBufferSetup,
        })
