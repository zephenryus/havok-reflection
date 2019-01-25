import struct


class hkaiDirectedGraphExplicitCostEdge(object):
    cost: int
    flags: any
    target: int

    def __init__(self, infile):
        self.cost = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT16
        self.target = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} cost={cost}, flags={flags}, target={target}>".format(**{
            "class_name": self.__class__.__name__,
            "cost": self.cost,
            "flags": self.flags,
            "target": self.target,
        })
