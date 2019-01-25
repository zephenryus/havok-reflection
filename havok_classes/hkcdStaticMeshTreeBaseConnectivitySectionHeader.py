import struct


class hkcdStaticMeshTreeBaseConnectivitySectionHeader(object):
    baseLocal: int
    baseGlobal: int

    def __init__(self, infile):
        self.baseLocal = struct.unpack('>I', infile.read(4))
        self.baseGlobal = struct.unpack('>I', infile.read(4))
