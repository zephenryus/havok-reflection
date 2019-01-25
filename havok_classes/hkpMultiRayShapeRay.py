import struct


class hkpMultiRayShapeRay(object):
    start: vector4
    end: vector4

    def __init__(self, infile):
        self.start = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.end = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} start={start}, end={end}>".format(**{
            "class_name": self.__class__.__name__,
            "start": self.start,
            "end": self.end,
        })
