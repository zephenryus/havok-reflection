from typing import List
from .common import get_array
from .hkpAgent1nSector import hkpAgent1nSector
from .hkpSerializedSubTrack1nInfo import hkpSerializedSubTrack1nInfo


class hkpSerializedTrack1nInfo(object):
    sectors: List[hkpAgent1nSector]
    subTracks: List[hkpSerializedSubTrack1nInfo]

    def __init__(self, infile):
        self.sectors = get_array(infile, hkpAgent1nSector, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.subTracks = get_array(infile, hkpSerializedSubTrack1nInfo, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} sectors=[{sectors}], subTracks=[{subTracks}]>".format(**{
            "class_name": self.__class__.__name__,
            "sectors": self.sectors,
            "subTracks": self.subTracks,
        })
