from .hkReferencedObject import hkReferencedObject
from .hkaiVolume import hkaiVolume


class hkaiMaterialPainter(hkReferencedObject):
	material: int
	volume: hkaiVolume
