from .hkaiNavMeshQueryMediator import hkaiNavMeshQueryMediator
from .hkaiStreamingCollection import hkaiStreamingCollection
from .hkcdDynamicAabbTree import hkcdDynamicAabbTree
from .hkaiNavMeshCutter import hkaiNavMeshCutter
import struct


class hkaiDynamicNavMeshQueryMediator(hkaiNavMeshQueryMediator):
    collection: any
    aabbTree: any
    cutter: any
    cutAabbTolerance: float

    def __init__(self, infile):
        self.collection = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.aabbTree = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.cutter = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.cutAabbTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} collection={collection}, aabbTree={aabbTree}, cutter={cutter}, cutAabbTolerance={cutAabbTolerance}>".format(**{
            "class_name": self.__class__.__name__,
            "collection": self.collection,
            "aabbTree": self.aabbTree,
            "cutter": self.cutter,
            "cutAabbTolerance": self.cutAabbTolerance,
        })
