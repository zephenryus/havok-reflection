import struct
from .hkAabb import hkAabb
from typing import List
from .common import get_array


class hkcdAdf(object):
    accuracy: float
    domain: hkAabb
    origin: vector4
    scale: vector4
    range: float
    nodes: List[int]
    voxels: List[int]

    def __init__(self, infile):
        self.accuracy = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.domain = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.origin = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.scale = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.range = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.nodes = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.voxels = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16

    def __repr__(self):
        return "<{class_name} accuracy={accuracy}, domain={domain}, origin={origin}, scale={scale}, range={range}, nodes=[{nodes}], voxels=[{voxels}]>".format(**{
            "class_name": self.__class__.__name__,
            "accuracy": self.accuracy,
            "domain": self.domain,
            "origin": self.origin,
            "scale": self.scale,
            "range": self.range,
            "nodes": self.nodes,
            "voxels": self.voxels,
        })
