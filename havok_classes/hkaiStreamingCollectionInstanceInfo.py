from .hkaiNavMeshInstance import hkaiNavMeshInstance
from .hkaiNavVolumeInstance import hkaiNavVolumeInstance
from .hkaiDirectedGraphInstance import hkaiDirectedGraphInstance
from .hkaiNavMeshQueryMediator import hkaiNavMeshQueryMediator
from .hkaiNavVolumeMediator import hkaiNavVolumeMediator
import struct


class hkaiStreamingCollectionInstanceInfo(object):
    instancePtr: hkaiNavMeshInstance
    volumeInstancePtr: hkaiNavVolumeInstance
    clusterGraphInstance: hkaiDirectedGraphInstance
    mediator: hkaiNavMeshQueryMediator
    volumeMediator: hkaiNavVolumeMediator
    treeNode: int

    def __init__(self, infile):
        self.instancePtr = hkaiNavMeshInstance(infile)  # TYPE_POINTER
        self.volumeInstancePtr = hkaiNavVolumeInstance(infile)  # TYPE_POINTER
        self.clusterGraphInstance = hkaiDirectedGraphInstance(infile)  # TYPE_POINTER
        self.mediator = hkaiNavMeshQueryMediator(infile)  # TYPE_POINTER
        self.volumeMediator = hkaiNavVolumeMediator(infile)  # TYPE_POINTER
        self.treeNode = struct.unpack('>I', infile.read(4))
