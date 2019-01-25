from .hclOperator import hclOperator
import struct
from typing import List
from .common import get_array


class hclSimulateOperator(hclOperator):
    simClothIndex: int
    subSteps: int
    numberOfSolveIterations: int
    constraintExecution: List[int]
    adaptConstraintStiffness: bool

    def __init__(self, infile):
        self.simClothIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.subSteps = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.numberOfSolveIterations = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.constraintExecution = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.adaptConstraintStiffness = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} simClothIndex={simClothIndex}, subSteps={subSteps}, numberOfSolveIterations={numberOfSolveIterations}, constraintExecution=[{constraintExecution}], adaptConstraintStiffness={adaptConstraintStiffness}>".format(**{
            "class_name": self.__class__.__name__,
            "simClothIndex": self.simClothIndex,
            "subSteps": self.subSteps,
            "numberOfSolveIterations": self.numberOfSolveIterations,
            "constraintExecution": self.constraintExecution,
            "adaptConstraintStiffness": self.adaptConstraintStiffness,
        })
