import struct


class hkpBroadPhaseHandle(object):
    id: int

    def __init__(self, infile):
        self.id = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} id={id}>".format(**{
            "class_name": self.__class__.__name__,
            "id": self.id,
        })
