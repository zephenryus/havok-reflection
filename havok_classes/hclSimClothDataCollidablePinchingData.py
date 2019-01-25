import struct


class hclSimClothDataCollidablePinchingData(object):
    pinchDetectionEnabled: bool
    pinchDetectionPriority: int
    pinchDetectionRadius: float

    def __init__(self, infile):
        self.pinchDetectionEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.pinchDetectionPriority = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.pinchDetectionRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} pinchDetectionEnabled={pinchDetectionEnabled}, pinchDetectionPriority={pinchDetectionPriority}, pinchDetectionRadius={pinchDetectionRadius}>".format(**{
            "class_name": self.__class__.__name__,
            "pinchDetectionEnabled": self.pinchDetectionEnabled,
            "pinchDetectionPriority": self.pinchDetectionPriority,
            "pinchDetectionRadius": self.pinchDetectionRadius,
        })
