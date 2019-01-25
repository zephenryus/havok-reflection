import struct


class hkSkinnedMeshShapeBoneSet(object):
    boneBufferOffset: int
    numBones: int

    def __init__(self, infile):
        self.boneBufferOffset = struct.unpack('>H', infile.read(2))
        self.numBones = struct.unpack('>H', infile.read(2))
