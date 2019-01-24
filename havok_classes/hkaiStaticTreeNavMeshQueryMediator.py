from .hkaiNavMeshQueryMediator import hkaiNavMeshQueryMediator
from .hkcdStaticAabbTree import hkcdStaticAabbTree
from .hkaiNavMesh import hkaiNavMesh


class hkaiStaticTreeNavMeshQueryMediator(hkaiNavMeshQueryMediator):
    tree: hkcdStaticAabbTree
    navMesh: hkaiNavMesh
