import struct


class hkMonitorStreamStringMapStringMap(object):
    id: int
    string: str

    def __init__(self, infile):
        self.id = struct.unpack('>Q', infile.read(8))
        self.string = struct.unpack('>s', infile.read(0))
