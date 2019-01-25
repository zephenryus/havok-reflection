from .hkaiNavMeshQueryMediator import hkaiNavMeshQueryMediator
from .hkcdStaticAabbTree import hkcdStaticAabbTree
from .hkaiNavMesh import hkaiNavMesh


class hkaiStaticTreeNavMeshQueryMediator(hkaiNavMeshQueryMediator):
    tree: any
    navMesh: any

    def __init__(self, infile):
        self.tree = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.navMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} tree={tree}, navMesh={navMesh}>".format(**{
            "class_name": self.__class__.__name__,
            "tree": self.tree,
            "navMesh": self.navMesh,
        })
