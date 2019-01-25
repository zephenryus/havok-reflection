import struct


class hkcdPlanarGeometryPrimitivesPlane(object):
    iEqn: int
    dEqn: int

    def __init__(self, infile):
        self.iEqn = struct.unpack('>q', infile.read(8))  # TYPE_INT64:TYPE_VOID
        self.dEqn = struct.unpack('>q', infile.read(8))  # TYPE_INT64:TYPE_VOID

    def __repr__(self):
        return "<{class_name} iEqn={iEqn}, dEqn={dEqn}>".format(**{
            "class_name": self.__class__.__name__,
            "iEqn": self.iEqn,
            "dEqn": self.dEqn,
        })
