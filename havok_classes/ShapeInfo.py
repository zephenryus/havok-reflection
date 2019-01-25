import struct


class ShapeInfo(object):
    ActorInfoIndex: int
    InstanceId: int
    BodyGroup: int
    BodyLayerType: int

    def __init__(self, infile):
        self.ActorInfoIndex = struct.unpack('>i', infile.read(4))
        self.InstanceId = struct.unpack('>i', infile.read(4))
        self.BodyGroup = struct.unpack('>b', infile.read(1))
        self.BodyLayerType = struct.unpack('>B', infile.read(1))
