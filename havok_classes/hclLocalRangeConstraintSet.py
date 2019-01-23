from .hclConstraintSet import hclConstraintSet
from .hclLocalRangeConstraintSetLocalConstraint import hclLocalRangeConstraintSetLocalConstraint


class hclLocalRangeConstraintSet(hclConstraintSet):
	localConstraints: hclLocalRangeConstraintSetLocalConstraint
	referenceMeshBufferIdx: int
	stiffness: float
	shapeType: any
	applyNormalComponent: bool
