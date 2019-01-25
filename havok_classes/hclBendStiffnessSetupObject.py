from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
import struct


class hclBendStiffnessSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: any
    vertexSelection: hclVertexSelectionInput
    bendStiffness: hclVertexFloatInput
    useRestPoseConfig: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simulationMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.bendStiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.useRestPoseConfig = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", simulationMesh={simulationMesh}, vertexSelection={vertexSelection}, bendStiffness={bendStiffness}, useRestPoseConfig={useRestPoseConfig}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "simulationMesh": self.simulationMesh,
            "vertexSelection": self.vertexSelection,
            "bendStiffness": self.bendStiffness,
            "useRestPoseConfig": self.useRestPoseConfig,
        })
