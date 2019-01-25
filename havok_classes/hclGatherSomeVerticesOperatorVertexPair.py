import struct


class hclGatherSomeVerticesOperatorVertexPair(object):
    indexInput: int
    indexOutput: int

    def __init__(self, infile):
        self.indexInput = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.indexOutput = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} indexInput={indexInput}, indexOutput={indexOutput}>".format(**{
            "class_name": self.__class__.__name__,
            "indexInput": self.indexInput,
            "indexOutput": self.indexOutput,
        })
