from .hclConstraintSet import hclConstraintSet
from .hclTransitionConstraintSetPerParticle import hclTransitionConstraintSetPerParticle


class hclTransitionConstraintSet(hclConstraintSet):
    perParticleData: hclTransitionConstraintSetPerParticle
    toAnimPeriod: float
    toAnimPlusDelayPeriod: float
    toSimPeriod: float
    toSimPlusDelayPeriod: float
    referenceMeshBufferIdx: int
