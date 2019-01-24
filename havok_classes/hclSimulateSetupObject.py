from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclSimClothSetupObject import hclSimClothSetupObject
from .hclConstraintSetSetupObject import hclConstraintSetSetupObject


class hclSimulateSetupObject(hclOperatorSetupObject):
    name: str
    simClothSetupObject: hclSimClothSetupObject
    numberOfSubsteps: int
    numberOfSolveIterations: int
    adaptConstraintStiffness: bool
    explicitConstraintOrder: bool
    constraintSetExecutionOrder: hclConstraintSetSetupObject
