from .hclOperator import hclOperator
import struct
from .common import any


class hclSimulateOperator(hclOperator):
    simClothIndex: int
    subSteps: int
    numberOfSolveIterations: int
    constraintExecution: any
    adaptConstraintStiffness: bool

    def __init__(self, infile):
        self.simClothIndex = struct.unpack('>I', infile.read(4))
        self.subSteps = struct.unpack('>I', infile.read(4))
        self.numberOfSolveIterations = struct.unpack('>i', infile.read(4))
        self.constraintExecution = any(infile)  # TYPE_ARRAY
        self.adaptConstraintStiffness = struct.unpack('>?', infile.read(1))
