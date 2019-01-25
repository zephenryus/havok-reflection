from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
import struct
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput


class hclBendLinkSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: any
    createStandardLinks: bool
    vertexSelection: hclVertexSelectionInput
    bendStiffness: hclVertexFloatInput
    stretchStiffness: hclVertexFloatInput
    flatnessFactor: hclVertexFloatInput

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simulationMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.createStandardLinks = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.bendStiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.stretchStiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.flatnessFactor = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", simulationMesh={simulationMesh}, createStandardLinks={createStandardLinks}, vertexSelection={vertexSelection}, bendStiffness={bendStiffness}, stretchStiffness={stretchStiffness}, flatnessFactor={flatnessFactor}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "simulationMesh": self.simulationMesh,
            "createStandardLinks": self.createStandardLinks,
            "vertexSelection": self.vertexSelection,
            "bendStiffness": self.bendStiffness,
            "stretchStiffness": self.stretchStiffness,
            "flatnessFactor": self.flatnessFactor,
        })
