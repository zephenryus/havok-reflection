import struct


class hkaiNavMeshEdge(object):
    a: int
    b: int
    oppositeEdge: int
    oppositeFace: int
    flags: any
    paddingByte: int
    userEdgeCost: int

    def __init__(self, infile):
        self.a = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.b = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.oppositeEdge = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.oppositeFace = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT8
        self.paddingByte = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.userEdgeCost = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID

    def __repr__(self):
        return "<{class_name} a={a}, b={b}, oppositeEdge={oppositeEdge}, oppositeFace={oppositeFace}, flags={flags}, paddingByte={paddingByte}, userEdgeCost={userEdgeCost}>".format(**{
            "class_name": self.__class__.__name__,
            "a": self.a,
            "b": self.b,
            "oppositeEdge": self.oppositeEdge,
            "oppositeFace": self.oppositeFace,
            "flags": self.flags,
            "paddingByte": self.paddingByte,
            "userEdgeCost": self.userEdgeCost,
        })
