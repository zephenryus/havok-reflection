import struct


class hkpBroadPhaseHandle(object):
    id: int

    def __init__(self, infile):
        self.id = struct.unpack('>I', infile.read(4))
