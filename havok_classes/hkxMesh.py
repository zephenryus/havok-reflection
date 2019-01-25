from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkxMeshSection import hkxMeshSection
from .hkxMeshUserChannelInfo import hkxMeshUserChannelInfo


class hkxMesh(hkReferencedObject):
    sections: List[hkxMeshSection]
    userChannelInfos: List[hkxMeshUserChannelInfo]

    def __init__(self, infile):
        self.sections = get_array(infile, hkxMeshSection, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.userChannelInfos = get_array(infile, hkxMeshUserChannelInfo, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} sections=[{sections}], userChannelInfos=[{userChannelInfos}]>".format(**{
            "class_name": self.__class__.__name__,
            "sections": self.sections,
            "userChannelInfos": self.userChannelInfos,
        })
