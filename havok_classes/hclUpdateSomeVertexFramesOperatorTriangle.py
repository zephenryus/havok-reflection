import struct


class hclUpdateSomeVertexFramesOperatorTriangle(object):
    indices: int

    def __init__(self, infile):
        self.indices = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} indices={indices}>".format(**{
            "class_name": self.__class__.__name__,
            "indices": self.indices,
        })
