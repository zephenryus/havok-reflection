from .hkcdStaticTreeTreehkcdStaticTreeDynamicStorage6 import hkcdStaticTreeTreehkcdStaticTreeDynamicStorage6
import struct
from .common import any
from .hkcdStaticPvsBlockHeader import hkcdStaticPvsBlockHeader


class hkcdStaticPvs(object):
    cells: hkcdStaticTreeTreehkcdStaticTreeDynamicStorage6
    bytesPerCells: int
    cellsPerBlock: int
    pvs: any
    map: any
    blocks: hkcdStaticPvsBlockHeader

    def __init__(self, infile):
        self.cells = hkcdStaticTreeTreehkcdStaticTreeDynamicStorage6(infile)  # TYPE_STRUCT
        self.bytesPerCells = struct.unpack('>i', infile.read(4))
        self.cellsPerBlock = struct.unpack('>i', infile.read(4))
        self.pvs = any(infile)  # TYPE_ARRAY
        self.map = any(infile)  # TYPE_ARRAY
        self.blocks = hkcdStaticPvsBlockHeader(infile)  # TYPE_ARRAY
