import struct


class hkaBone(object):
    name: str
    lockTranslation: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.lockTranslation = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", lockTranslation={lockTranslation}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "lockTranslation": self.lockTranslation,
        })
