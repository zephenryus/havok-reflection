from .hclBufferSetupObject import hclBufferSetupObject
from .hclSetupMesh import hclSetupMesh


class hclStaticDisplayBufferSetupObject(hclBufferSetupObject):
    setupMesh: hclSetupMesh
    name: str
