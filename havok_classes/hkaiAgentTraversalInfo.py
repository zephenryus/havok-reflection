import struct


class hkaiAgentTraversalInfo(object):
    diameter: float
    filterInfo: int

    def __init__(self, infile):
        self.diameter = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.filterInfo = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} diameter={diameter}, filterInfo={filterInfo}>".format(**{
            "class_name": self.__class__.__name__,
            "diameter": self.diameter,
            "filterInfo": self.filterInfo,
        })
