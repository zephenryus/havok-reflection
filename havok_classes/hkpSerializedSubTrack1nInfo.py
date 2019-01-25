from .hkpSerializedTrack1nInfo import hkpSerializedTrack1nInfo
import struct


class hkpSerializedSubTrack1nInfo(hkpSerializedTrack1nInfo):
    sectorIndex: int
    offsetInSector: int

    def __init__(self, infile):
        self.sectorIndex = struct.unpack('>i', infile.read(4))
        self.offsetInSector = struct.unpack('>i', infile.read(4))
