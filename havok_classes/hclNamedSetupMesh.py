from .hclSetupMesh import hclSetupMesh


class hclNamedSetupMesh(hclSetupMesh):
    name: str
    meshName: str
    setupMesh: hclSetupMesh
