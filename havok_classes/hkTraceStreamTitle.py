import struct


class hkTraceStreamTitle(object):
    value: str

    def __init__(self, infile):
        self.value = struct.unpack('>c', infile.read(1))  # TYPE_CHAR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} value=\"{value}\">".format(**{
            "class_name": self.__class__.__name__,
            "value": self.value,
        })
