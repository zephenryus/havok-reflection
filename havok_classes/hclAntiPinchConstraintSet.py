from .hclConstraintSet import hclConstraintSet
from .hclAntiPinchConstraintSetPerParticle import hclAntiPinchConstraintSetPerParticle


class hclAntiPinchConstraintSet(hclConstraintSet):
	perParticleData: hclAntiPinchConstraintSetPerParticle
	toAnimPeriod: float
	toSimPeriod: float
	toSimMaxDistance: float
	referenceMeshBufferIdx: int
