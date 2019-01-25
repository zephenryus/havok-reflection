from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
import struct
from .enums import ShapeType


class hclLocalRangeSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: any
    referenceBufferSetup: any
    vertexSelection: hclVertexSelectionInput
    maximumDistance: hclVertexFloatInput
    minNormalDistance: hclVertexFloatInput
    maxNormalDistance: hclVertexFloatInput
    stiffness: float
    localRangeShape: ShapeType
    useMinNormalDistance: bool
    useMaxNormalDistance: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simulationMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.referenceBufferSetup = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.maximumDistance = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.minNormalDistance = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.maxNormalDistance = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.stiffness = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.localRangeShape = ShapeType(infile)  # TYPE_ENUM:TYPE_UINT32
        self.useMinNormalDistance = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.useMaxNormalDistance = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", simulationMesh={simulationMesh}, referenceBufferSetup={referenceBufferSetup}, vertexSelection={vertexSelection}, maximumDistance={maximumDistance}, minNormalDistance={minNormalDistance}, maxNormalDistance={maxNormalDistance}, stiffness={stiffness}, localRangeShape={localRangeShape}, useMinNormalDistance={useMinNormalDistance}, useMaxNormalDistance={useMaxNormalDistance}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "simulationMesh": self.simulationMesh,
            "referenceBufferSetup": self.referenceBufferSetup,
            "vertexSelection": self.vertexSelection,
            "maximumDistance": self.maximumDistance,
            "minNormalDistance": self.minNormalDistance,
            "maxNormalDistance": self.maxNormalDistance,
            "stiffness": self.stiffness,
            "localRangeShape": self.localRangeShape,
            "useMinNormalDistance": self.useMinNormalDistance,
            "useMaxNormalDistance": self.useMaxNormalDistance,
        })
