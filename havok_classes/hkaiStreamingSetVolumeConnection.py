import struct


class hkaiStreamingSetVolumeConnection(object):
    cellIndex: int
    oppositeCellIndex: int

    def __init__(self, infile):
        self.cellIndex = struct.unpack('>i', infile.read(4))
        self.oppositeCellIndex = struct.unpack('>i', infile.read(4))
