from .hkReferencedObject import hkReferencedObject
from .hkxMeshSection import hkxMeshSection
from .hkxMeshUserChannelInfo import hkxMeshUserChannelInfo


class hkxMesh(hkReferencedObject):
    sections: hkxMeshSection
    userChannelInfos: hkxMeshUserChannelInfo
