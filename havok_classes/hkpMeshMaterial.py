import struct


class hkpMeshMaterial(object):
    filterInfo: int

    def __init__(self, infile):
        self.filterInfo = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} filterInfo={filterInfo}>".format(**{
            "class_name": self.__class__.__name__,
            "filterInfo": self.filterInfo,
        })
