import struct


class hkaiEdgePathFollowingCornerInfo(object):
    data: int

    def __init__(self, infile):
        self.data = struct.unpack('>H', infile.read(2))
