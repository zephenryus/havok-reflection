import struct


class hkaiNavMeshGenerationSettingsMaterialConstructionPair(object):
    materialIndex: int
    flags: any

    def __init__(self, infile):
        self.materialIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT32

    def __repr__(self):
        return "<{class_name} materialIndex={materialIndex}, flags={flags}>".format(**{
            "class_name": self.__class__.__name__,
            "materialIndex": self.materialIndex,
            "flags": self.flags,
        })
