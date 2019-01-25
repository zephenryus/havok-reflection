import struct


class hkcdStaticMeshTreeBaseConnectivitySectionHeader(object):
    baseLocal: int
    baseGlobal: int

    def __init__(self, infile):
        self.baseLocal = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.baseGlobal = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} baseLocal={baseLocal}, baseGlobal={baseGlobal}>".format(**{
            "class_name": self.__class__.__name__,
            "baseLocal": self.baseLocal,
            "baseGlobal": self.baseGlobal,
        })
