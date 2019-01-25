import struct


class hkxNodeAnnotationData(object):
    time: float
    description: str

    def __init__(self, infile):
        self.time = struct.unpack('>f', infile.read(4))
        self.description = struct.unpack('>s', infile.read(0))
