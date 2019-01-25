import struct


class hclSimClothDataCollidablePinchingData(object):
    pinchDetectionEnabled: bool
    pinchDetectionPriority: int
    pinchDetectionRadius: float

    def __init__(self, infile):
        self.pinchDetectionEnabled = struct.unpack('>?', infile.read(1))
        self.pinchDetectionPriority = struct.unpack('>b', infile.read(1))
        self.pinchDetectionRadius = struct.unpack('>f', infile.read(4))
