import struct


class hkaiEdgeGeometryFace(object):
    data: int
    faceIndex: int
    flags: any

    def __init__(self, infile):
        self.data = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.faceIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} data={data}, faceIndex={faceIndex}, flags={flags}>".format(**{
            "class_name": self.__class__.__name__,
            "data": self.data,
            "faceIndex": self.faceIndex,
            "flags": self.flags,
        })
