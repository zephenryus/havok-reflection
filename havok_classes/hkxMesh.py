from .hkReferencedObject import hkReferencedObject
from .hkxMeshSection import hkxMeshSection
from .hkxMeshUserChannelInfo import hkxMeshUserChannelInfo


class hkxMesh(hkReferencedObject):
    sections: hkxMeshSection
    userChannelInfos: hkxMeshUserChannelInfo

    def __init__(self, infile):
        self.sections = hkxMeshSection(infile)  # TYPE_ARRAY
        self.userChannelInfos = hkxMeshUserChannelInfo(infile)  # TYPE_ARRAY
