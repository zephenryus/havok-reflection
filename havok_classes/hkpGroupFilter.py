from .hkpCollisionFilter import hkpCollisionFilter


class hkpGroupFilter(hkpCollisionFilter):
	nextFreeSystemGroup: int
	collisionLookupTable: int
	pad256: any
