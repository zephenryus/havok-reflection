import struct


class hkpAgent1nSector(object):
    bytesAllocated: int
    pad0: int
    pad1: int
    pad2: int
    data: int

    def __init__(self, infile):
        self.bytesAllocated = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.pad0 = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.pad1 = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.pad2 = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.data = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} bytesAllocated={bytesAllocated}, pad0={pad0}, pad1={pad1}, pad2={pad2}, data={data}>".format(**{
            "class_name": self.__class__.__name__,
            "bytesAllocated": self.bytesAllocated,
            "pad0": self.pad0,
            "pad1": self.pad1,
            "pad2": self.pad2,
            "data": self.data,
        })
