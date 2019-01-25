import struct


class hkcdStaticMeshTreeBaseEdge(object):
    keyAndIndex: int

    def __init__(self, infile):
        self.keyAndIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} keyAndIndex={keyAndIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "keyAndIndex": self.keyAndIndex,
        })
