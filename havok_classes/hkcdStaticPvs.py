from .hkcdStaticTreeTreehkcdStaticTreeDynamicStorage6 import hkcdStaticTreeTreehkcdStaticTreeDynamicStorage6
from .hkcdStaticPvsBlockHeader import hkcdStaticPvsBlockHeader


class hkcdStaticPvs(object):
	cells: hkcdStaticTreeTreehkcdStaticTreeDynamicStorage6
	bytesPerCells: int
	cellsPerBlock: int
	pvs: any
	map: any
	blocks: hkcdStaticPvsBlockHeader
