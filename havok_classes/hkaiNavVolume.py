from .hkReferencedObject import hkReferencedObject
from .hkaiNavVolumeCell import hkaiNavVolumeCell
from .hkaiNavVolumeEdge import hkaiNavVolumeEdge
from .hkaiStreamingSet import hkaiStreamingSet
from .hkAabb import hkAabb


class hkaiNavVolume(hkReferencedObject):
	cells: hkaiNavVolumeCell
	edges: hkaiNavVolumeEdge
	streamingSets: hkaiStreamingSet
	aabb: hkAabb
	quantizationScale: any
	quantizationOffset: any
	res: int
	userData: int
