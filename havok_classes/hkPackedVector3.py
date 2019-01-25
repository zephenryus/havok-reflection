import struct


class hkPackedVector3(object):
    values: int

    def __init__(self, infile):
        self.values = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} values={values}>".format(**{
            "class_name": self.__class__.__name__,
            "values": self.values,
        })
