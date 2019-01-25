import struct


class hkaiNavMeshClearanceCacheMcpDataInteger(object):
    interpolant: int
    clearance: int

    def __init__(self, infile):
        self.interpolant = struct.unpack('>B', infile.read(1))
        self.clearance = struct.unpack('>B', infile.read(1))
