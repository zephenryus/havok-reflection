import struct


class hclBlendSomeVerticesOperatorBlendEntry(object):
    vertexIndex: int
    blendWeight: float

    def __init__(self, infile):
        self.vertexIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.blendWeight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexIndex={vertexIndex}, blendWeight={blendWeight}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexIndex": self.vertexIndex,
            "blendWeight": self.blendWeight,
        })
