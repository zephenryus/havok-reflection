from .hclBufferSetupObject import hclBufferSetupObject
from .hclSetupMesh import hclSetupMesh


class hclStaticDisplayBufferSetupObject(hclBufferSetupObject):
    setupMesh: hclSetupMesh
    name: str

    def __init__(self, infile):
        self.setupMesh = hclSetupMesh(infile)  # TYPE_POINTER
        self.name = struct.unpack('>s', infile.read(0))
