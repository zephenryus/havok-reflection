import struct


class hkaiNavVolumeEdge(object):
    flags: any
    oppositeCell: int

    def __init__(self, infile):
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT8
        self.oppositeCell = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} flags={flags}, oppositeCell={oppositeCell}>".format(**{
            "class_name": self.__class__.__name__,
            "flags": self.flags,
            "oppositeCell": self.oppositeCell,
        })
