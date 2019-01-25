import struct


class hkaiNavMeshClearanceCacheMcpDataInteger(object):
    interpolant: int
    clearance: int

    def __init__(self, infile):
        self.interpolant = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.clearance = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} interpolant={interpolant}, clearance={clearance}>".format(**{
            "class_name": self.__class__.__name__,
            "interpolant": self.interpolant,
            "clearance": self.clearance,
        })
