import struct


class hkaiPersistentFaceKey(object):
    key: int
    offset: int

    def __init__(self, infile):
        self.key = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.offset = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} key={key}, offset={offset}>".format(**{
            "class_name": self.__class__.__name__,
            "key": self.key,
            "offset": self.offset,
        })
