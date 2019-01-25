import struct


class hkaBone(object):
    name: str
    lockTranslation: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.lockTranslation = struct.unpack('>?', infile.read(1))
