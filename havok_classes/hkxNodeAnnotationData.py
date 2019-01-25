import struct


class hkxNodeAnnotationData(object):
    time: float
    description: str

    def __init__(self, infile):
        self.time = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.description = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} time={time}, description=\"{description}\">".format(**{
            "class_name": self.__class__.__name__,
            "time": self.time,
            "description": self.description,
        })
