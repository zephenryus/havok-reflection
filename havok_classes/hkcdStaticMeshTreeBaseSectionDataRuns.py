import struct


class hkcdStaticMeshTreeBaseSectionDataRuns(object):
    data: int

    def __init__(self, infile):
        self.data = struct.unpack('>I', infile.read(4))
