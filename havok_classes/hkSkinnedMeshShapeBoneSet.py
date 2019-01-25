import struct


class hkSkinnedMeshShapeBoneSet(object):
    boneBufferOffset: int
    numBones: int

    def __init__(self, infile):
        self.boneBufferOffset = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.numBones = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} boneBufferOffset={boneBufferOffset}, numBones={numBones}>".format(**{
            "class_name": self.__class__.__name__,
            "boneBufferOffset": self.boneBufferOffset,
            "numBones": self.numBones,
        })
