from .hkpSerializedTrack1nInfo import hkpSerializedTrack1nInfo
import struct


class hkpSerializedSubTrack1nInfo(hkpSerializedTrack1nInfo):
    sectorIndex: int
    offsetInSector: int

    def __init__(self, infile):
        self.sectorIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.offsetInSector = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} sectorIndex={sectorIndex}, offsetInSector={offsetInSector}>".format(**{
            "class_name": self.__class__.__name__,
            "sectorIndex": self.sectorIndex,
            "offsetInSector": self.offsetInSector,
        })
