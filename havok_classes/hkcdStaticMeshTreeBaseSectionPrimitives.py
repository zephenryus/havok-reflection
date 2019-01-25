import struct


class hkcdStaticMeshTreeBaseSectionPrimitives(object):
    data: int

    def __init__(self, infile):
        self.data = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} data={data}>".format(**{
            "class_name": self.__class__.__name__,
            "data": self.data,
        })
