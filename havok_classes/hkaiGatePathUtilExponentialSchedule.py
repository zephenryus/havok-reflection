import struct


class hkaiGatePathUtilExponentialSchedule(object):
    round: int

    def __init__(self, infile):
        self.round = struct.unpack('>i', infile.read(4))
