import struct


class hkaiAgentTraversalInfo(object):
    diameter: float
    filterInfo: int

    def __init__(self, infile):
        self.diameter = struct.unpack('>f', infile.read(4))
        self.filterInfo = struct.unpack('>I', infile.read(4))
