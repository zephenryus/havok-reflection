from .hkaiNavMeshQueryMediator import hkaiNavMeshQueryMediator
from .hkcdStaticAabbTree import hkcdStaticAabbTree
from .hkaiNavMesh import hkaiNavMesh


class hkaiStaticTreeNavMeshQueryMediator(hkaiNavMeshQueryMediator):
    tree: hkcdStaticAabbTree
    navMesh: hkaiNavMesh

    def __init__(self, infile):
        self.tree = hkcdStaticAabbTree(infile)  # TYPE_POINTER
        self.navMesh = hkaiNavMesh(infile)  # TYPE_POINTER
