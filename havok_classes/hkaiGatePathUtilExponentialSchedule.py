import struct


class hkaiGatePathUtilExponentialSchedule(object):
    round: int

    def __init__(self, infile):
        self.round = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} round={round}>".format(**{
            "class_name": self.__class__.__name__,
            "round": self.round,
        })
