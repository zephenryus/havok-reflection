import struct


class hkClassEnumItem(object):
    value: int
    name: str

    def __init__(self, infile):
        self.value = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.name = str(infile)  # TYPE_CSTRING:TYPE_VOID

    def __repr__(self):
        return "<{class_name} value={value}, name=\"{name}\">".format(**{
            "class_name": self.__class__.__name__,
            "value": self.value,
            "name": self.name,
        })
