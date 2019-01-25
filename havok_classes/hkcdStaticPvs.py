from .hkcdStaticTreeTreehkcdStaticTreeDynamicStorage6 import hkcdStaticTreeTreehkcdStaticTreeDynamicStorage6
import struct
from typing import List
from .common import get_array
from .hkcdStaticPvsBlockHeader import hkcdStaticPvsBlockHeader


class hkcdStaticPvs(object):
    cells: hkcdStaticTreeTreehkcdStaticTreeDynamicStorage6
    bytesPerCells: int
    cellsPerBlock: int
    pvs: List[int]
    map: List[int]
    blocks: List[hkcdStaticPvsBlockHeader]

    def __init__(self, infile):
        self.cells = hkcdStaticTreeTreehkcdStaticTreeDynamicStorage6(infile)  # TYPE_STRUCT:TYPE_VOID
        self.bytesPerCells = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.cellsPerBlock = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.pvs = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.map = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.blocks = get_array(infile, hkcdStaticPvsBlockHeader, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} cells={cells}, bytesPerCells={bytesPerCells}, cellsPerBlock={cellsPerBlock}, pvs=[{pvs}], map=[{map}], blocks=[{blocks}]>".format(**{
            "class_name": self.__class__.__name__,
            "cells": self.cells,
            "bytesPerCells": self.bytesPerCells,
            "cellsPerBlock": self.cellsPerBlock,
            "pvs": self.pvs,
            "map": self.map,
            "blocks": self.blocks,
        })
