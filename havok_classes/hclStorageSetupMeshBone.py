from .common import any


class hclStorageSetupMeshBone(object):
    name: str
    boneFromSkin: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.boneFromSkin = any(infile)  # TYPE_MATRIX4
