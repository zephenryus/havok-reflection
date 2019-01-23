from .hkReferencedObject import hkReferencedObject
from .hkaiNavVolume import hkaiNavVolume
from .hkaiNavVolumeInstanceCellInstance import hkaiNavVolumeInstanceCellInstance
from .hkaiNavVolumeEdge import hkaiNavVolumeEdge


class hkaiNavVolumeInstance(hkReferencedObject):
	originalCells: any
	originalEdges: any
	originalVolume: hkaiNavVolume
	cellMap: any
	instancedCells: hkaiNavVolumeInstanceCellInstance
	ownedEdges: hkaiNavVolumeEdge
	sectionUid: int
	runtimeId: int
	layer: int
	translation: any