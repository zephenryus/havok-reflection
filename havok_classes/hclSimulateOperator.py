from .hclOperator import hclOperator
from .common import any


class hclSimulateOperator(hclOperator):
    simClothIndex: int
    subSteps: int
    numberOfSolveIterations: int
    constraintExecution: any
    adaptConstraintStiffness: bool
