import struct


class ActorInfo(object):
    HashId: int
    SRTHash: int
    ShapeInfoStart: int
    ShapeInfoEnd: int

    def __init__(self, infile):
        self.HashId = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.SRTHash = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.ShapeInfoStart = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.ShapeInfoEnd = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} HashId={HashId}, SRTHash={SRTHash}, ShapeInfoStart={ShapeInfoStart}, ShapeInfoEnd={ShapeInfoEnd}>".format(**{
            "class_name": self.__class__.__name__,
            "HashId": self.HashId,
            "SRTHash": self.SRTHash,
            "ShapeInfoStart": self.ShapeInfoStart,
            "ShapeInfoEnd": self.ShapeInfoEnd,
        })
