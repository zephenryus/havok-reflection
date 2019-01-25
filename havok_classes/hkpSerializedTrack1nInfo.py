from .hkpAgent1nSector import hkpAgent1nSector
from .hkpSerializedSubTrack1nInfo import hkpSerializedSubTrack1nInfo


class hkpSerializedTrack1nInfo(object):
    sectors: hkpAgent1nSector
    subTracks: hkpSerializedSubTrack1nInfo

    def __init__(self, infile):
        self.sectors = hkpAgent1nSector(infile)  # TYPE_ARRAY
        self.subTracks = hkpSerializedSubTrack1nInfo(infile)  # TYPE_ARRAY
