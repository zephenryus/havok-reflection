import struct


class hkMonitorStreamStringMapStringMap(object):
    id: int
    string: str

    def __init__(self, infile):
        self.id = struct.unpack('>Q', infile.read(8))  # TYPE_UINT64:TYPE_VOID
        self.string = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} id={id}, string=\"{string}\">".format(**{
            "class_name": self.__class__.__name__,
            "id": self.id,
            "string": self.string,
        })
