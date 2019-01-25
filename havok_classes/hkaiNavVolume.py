from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
from .hkaiNavVolumeCell import hkaiNavVolumeCell
from .hkaiNavVolumeEdge import hkaiNavVolumeEdge
from .hkaiStreamingSet import hkaiStreamingSet
from .hkAabb import hkAabb
import struct


class Constants(Enum):
    INVALID_CELL_INDEX = 4294967295
    INVALID_EDGE_INDEX = 4294967295


class CellEdgeFlagBits(Enum):
    EDGE_EXTERNAL_OPPOSITE = 64


class hkaiNavVolume(hkReferencedObject):
    cells: List[hkaiNavVolumeCell]
    edges: List[hkaiNavVolumeEdge]
    streamingSets: List[hkaiStreamingSet]
    aabb: hkAabb
    quantizationScale: vector4
    quantizationOffset: vector4
    res: int
    userData: int

    def __init__(self, infile):
        self.cells = get_array(infile, hkaiNavVolumeCell, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.edges = get_array(infile, hkaiNavVolumeEdge, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.streamingSets = get_array(infile, hkaiStreamingSet, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.aabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.quantizationScale = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.quantizationOffset = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.res = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID

    def __repr__(self):
        return "<{class_name} cells=[{cells}], edges=[{edges}], streamingSets=[{streamingSets}], aabb={aabb}, quantizationScale={quantizationScale}, quantizationOffset={quantizationOffset}, res={res}, userData={userData}>".format(**{
            "class_name": self.__class__.__name__,
            "cells": self.cells,
            "edges": self.edges,
            "streamingSets": self.streamingSets,
            "aabb": self.aabb,
            "quantizationScale": self.quantizationScale,
            "quantizationOffset": self.quantizationOffset,
            "res": self.res,
            "userData": self.userData,
        })
