import struct
from .hkaiStreamingSetNavMeshConnection import hkaiStreamingSetNavMeshConnection
from .hkaiStreamingSetGraphConnection import hkaiStreamingSetGraphConnection
from .hkaiStreamingSetVolumeConnection import hkaiStreamingSetVolumeConnection


class hkaiStreamingSet(object):
    thisUid: int
    oppositeUid: int
    meshConnections: hkaiStreamingSetNavMeshConnection
    graphConnections: hkaiStreamingSetGraphConnection
    volumeConnections: hkaiStreamingSetVolumeConnection

    def __init__(self, infile):
        self.thisUid = struct.unpack('>I', infile.read(4))
        self.oppositeUid = struct.unpack('>I', infile.read(4))
        self.meshConnections = hkaiStreamingSetNavMeshConnection(infile)  # TYPE_ARRAY
        self.graphConnections = hkaiStreamingSetGraphConnection(infile)  # TYPE_ARRAY
        self.volumeConnections = hkaiStreamingSetVolumeConnection(infile)  # TYPE_ARRAY
