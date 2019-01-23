from .hclOperator import hclOperator


class hclSimulateOperator(hclOperator):
	simClothIndex: int
	subSteps: int
	numberOfSolveIterations: int
	constraintExecution: any
	adaptConstraintStiffness: bool
