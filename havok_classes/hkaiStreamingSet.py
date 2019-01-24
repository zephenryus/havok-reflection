from .hkaiStreamingSetNavMeshConnection import hkaiStreamingSetNavMeshConnection
from .hkaiStreamingSetGraphConnection import hkaiStreamingSetGraphConnection
from .hkaiStreamingSetVolumeConnection import hkaiStreamingSetVolumeConnection


class hkaiStreamingSet(object):
    thisUid: int
    oppositeUid: int
    meshConnections: hkaiStreamingSetNavMeshConnection
    graphConnections: hkaiStreamingSetGraphConnection
    volumeConnections: hkaiStreamingSetVolumeConnection
