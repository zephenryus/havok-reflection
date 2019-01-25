import struct


class hkaiNavVolumeGenerationSettingsMaterialConstructionInfo(object):
    materialIndex: int
    flags: any
    resolution: int

    def __init__(self, infile):
        self.materialIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT32
        self.resolution = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} materialIndex={materialIndex}, flags={flags}, resolution={resolution}>".format(**{
            "class_name": self.__class__.__name__,
            "materialIndex": self.materialIndex,
            "flags": self.flags,
            "resolution": self.resolution,
        })
