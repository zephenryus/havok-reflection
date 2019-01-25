import struct
from .ActorInfo import ActorInfo
from .ShapeInfo import ShapeInfo


class StaticCompoundInfo(object):
    Offset: int
    ActorInfo: ActorInfo
    ShapeInfo: ShapeInfo

    def __init__(self, infile):
        self.Offset = struct.unpack('>I', infile.read(4))
        self.ActorInfo = ActorInfo(infile)  # TYPE_ARRAY
        self.ShapeInfo = ShapeInfo(infile)  # TYPE_ARRAY
