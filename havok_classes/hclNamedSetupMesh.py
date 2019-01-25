from .hclSetupMesh import hclSetupMesh


class hclNamedSetupMesh(hclSetupMesh):
    name: str
    meshName: str
    setupMesh: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.meshName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.setupMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} name=\"{name}\", meshName=\"{meshName}\", setupMesh={setupMesh}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "meshName": self.meshName,
            "setupMesh": self.setupMesh,
        })
