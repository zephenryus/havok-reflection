import struct


class ShapeInfo(object):
    ActorInfoIndex: int
    InstanceId: int
    BodyGroup: int
    BodyLayerType: int

    def __init__(self, infile):
        self.ActorInfoIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.InstanceId = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.BodyGroup = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.BodyLayerType = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} ActorInfoIndex={ActorInfoIndex}, InstanceId={InstanceId}, BodyGroup={BodyGroup}, BodyLayerType={BodyLayerType}>".format(**{
            "class_name": self.__class__.__name__,
            "ActorInfoIndex": self.ActorInfoIndex,
            "InstanceId": self.InstanceId,
            "BodyGroup": self.BodyGroup,
            "BodyLayerType": self.BodyLayerType,
        })
