import struct


class hkpMeshMaterial(object):
    filterInfo: int

    def __init__(self, infile):
        self.filterInfo = struct.unpack('>I', infile.read(4))
