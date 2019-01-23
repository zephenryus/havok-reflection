from .hkaiNavVolumeMediator import hkaiNavVolumeMediator
from .hkaiNavVolume import hkaiNavVolume
from .hkcdStaticAabbTree import hkcdStaticAabbTree


class hkaiAabbTreeNavVolumeMediator(hkaiNavVolumeMediator):
	navVolume: hkaiNavVolume
	tree: hkcdStaticAabbTree
