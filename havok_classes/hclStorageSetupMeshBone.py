class hclStorageSetupMeshBone(object):
    name: str
    boneFromSkin: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.boneFromSkin = any(infile)  # TYPE_MATRIX4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", boneFromSkin={boneFromSkin}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "boneFromSkin": self.boneFromSkin,
        })
