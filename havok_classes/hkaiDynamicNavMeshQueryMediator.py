from .hkaiNavMeshQueryMediator import hkaiNavMeshQueryMediator
from .hkaiStreamingCollection import hkaiStreamingCollection
from .hkcdDynamicAabbTree import hkcdDynamicAabbTree
from .hkaiNavMeshCutter import hkaiNavMeshCutter
import struct


class hkaiDynamicNavMeshQueryMediator(hkaiNavMeshQueryMediator):
    collection: hkaiStreamingCollection
    aabbTree: hkcdDynamicAabbTree
    cutter: hkaiNavMeshCutter
    cutAabbTolerance: float

    def __init__(self, infile):
        self.collection = hkaiStreamingCollection(infile)  # TYPE_POINTER
        self.aabbTree = hkcdDynamicAabbTree(infile)  # TYPE_POINTER
        self.cutter = hkaiNavMeshCutter(infile)  # TYPE_POINTER
        self.cutAabbTolerance = struct.unpack('>f', infile.read(4))
