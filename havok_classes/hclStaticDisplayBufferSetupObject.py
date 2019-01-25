from .hclBufferSetupObject import hclBufferSetupObject
from .hclSetupMesh import hclSetupMesh


class hclStaticDisplayBufferSetupObject(hclBufferSetupObject):
    setupMesh: any
    name: str

    def __init__(self, infile):
        self.setupMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} setupMesh={setupMesh}, name=\"{name}\">".format(**{
            "class_name": self.__class__.__name__,
            "setupMesh": self.setupMesh,
            "name": self.name,
        })
