import struct


class hkaiAdaptiveRanger(object):
    curRange: float

    def __init__(self, infile):
        self.curRange = struct.unpack('>f', infile.read(4))
