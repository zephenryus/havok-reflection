import struct
from typing import List
from .common import get_array
from .hkaiStreamingSetNavMeshConnection import hkaiStreamingSetNavMeshConnection
from .hkaiStreamingSetGraphConnection import hkaiStreamingSetGraphConnection
from .hkaiStreamingSetVolumeConnection import hkaiStreamingSetVolumeConnection


class hkaiStreamingSet(object):
    thisUid: int
    oppositeUid: int
    meshConnections: List[hkaiStreamingSetNavMeshConnection]
    graphConnections: List[hkaiStreamingSetGraphConnection]
    volumeConnections: List[hkaiStreamingSetVolumeConnection]

    def __init__(self, infile):
        self.thisUid = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.oppositeUid = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.meshConnections = get_array(infile, hkaiStreamingSetNavMeshConnection, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.graphConnections = get_array(infile, hkaiStreamingSetGraphConnection, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.volumeConnections = get_array(infile, hkaiStreamingSetVolumeConnection, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} thisUid={thisUid}, oppositeUid={oppositeUid}, meshConnections=[{meshConnections}], graphConnections=[{graphConnections}], volumeConnections=[{volumeConnections}]>".format(**{
            "class_name": self.__class__.__name__,
            "thisUid": self.thisUid,
            "oppositeUid": self.oppositeUid,
            "meshConnections": self.meshConnections,
            "graphConnections": self.graphConnections,
            "volumeConnections": self.volumeConnections,
        })
