from .hkpPhantom import hkpPhantom
from .hkAabb import hkAabb


class hkpAabbPhantom(hkpPhantom):
	aabb: hkAabb
	overlappingCollidables: any
	orderDirty: bool
