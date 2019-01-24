from .hkaiNavMeshInstance import hkaiNavMeshInstance
from .hkaiNavVolumeInstance import hkaiNavVolumeInstance
from .hkaiDirectedGraphInstance import hkaiDirectedGraphInstance
from .hkaiNavMeshQueryMediator import hkaiNavMeshQueryMediator
from .hkaiNavVolumeMediator import hkaiNavVolumeMediator


class hkaiStreamingCollectionInstanceInfo(object):
    instancePtr: hkaiNavMeshInstance
    volumeInstancePtr: hkaiNavVolumeInstance
    clusterGraphInstance: hkaiDirectedGraphInstance
    mediator: hkaiNavMeshQueryMediator
    volumeMediator: hkaiNavVolumeMediator
    treeNode: int
