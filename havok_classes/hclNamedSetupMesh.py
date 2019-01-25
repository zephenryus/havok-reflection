from .hclSetupMesh import hclSetupMesh


class hclNamedSetupMesh(hclSetupMesh):
    name: str
    meshName: str
    setupMesh: hclSetupMesh

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.meshName = struct.unpack('>s', infile.read(0))
        self.setupMesh = hclSetupMesh(infile)  # TYPE_POINTER
