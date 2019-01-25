from .hkaiNavMeshInstance import hkaiNavMeshInstance
from .hkaiNavVolumeInstance import hkaiNavVolumeInstance
from .hkaiDirectedGraphInstance import hkaiDirectedGraphInstance
from .hkaiNavMeshQueryMediator import hkaiNavMeshQueryMediator
from .hkaiNavVolumeMediator import hkaiNavVolumeMediator
import struct


class hkaiStreamingCollectionInstanceInfo(object):
    instancePtr: any
    volumeInstancePtr: any
    clusterGraphInstance: any
    mediator: any
    volumeMediator: any
    treeNode: int

    def __init__(self, infile):
        self.instancePtr = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.volumeInstancePtr = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.clusterGraphInstance = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.mediator = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.volumeMediator = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.treeNode = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} instancePtr={instancePtr}, volumeInstancePtr={volumeInstancePtr}, clusterGraphInstance={clusterGraphInstance}, mediator={mediator}, volumeMediator={volumeMediator}, treeNode={treeNode}>".format(**{
            "class_name": self.__class__.__name__,
            "instancePtr": self.instancePtr,
            "volumeInstancePtr": self.volumeInstancePtr,
            "clusterGraphInstance": self.clusterGraphInstance,
            "mediator": self.mediator,
            "volumeMediator": self.volumeMediator,
            "treeNode": self.treeNode,
        })
