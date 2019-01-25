import struct


class hkxMaterialProperty(object):
    key: int
    value: int

    def __init__(self, infile):
        self.key = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.value = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} key={key}, value={value}>".format(**{
            "class_name": self.__class__.__name__,
            "key": self.key,
            "value": self.value,
        })
