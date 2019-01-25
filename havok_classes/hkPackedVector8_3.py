import struct


class hkPackedVector8_3(object):
    values: int

    def __init__(self, infile):
        self.values = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} values={values}>".format(**{
            "class_name": self.__class__.__name__,
            "values": self.values,
        })
