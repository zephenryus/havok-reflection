from .hkpFirstPersonGun import hkpFirstPersonGun
import struct
from typing import List
from .common import get_array


class hkpProjectileGun(hkpFirstPersonGun):
    maxProjectiles: int
    reloadTime: float
    reload: float
    projectiles: List[any]
    world: any
    destructionWorld: any

    def __init__(self, infile):
        self.maxProjectiles = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.reloadTime = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.reload = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.projectiles = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.world = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.destructionWorld = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} maxProjectiles={maxProjectiles}, reloadTime={reloadTime}, reload={reload}, projectiles=[{projectiles}], world={world}, destructionWorld={destructionWorld}>".format(**{
            "class_name": self.__class__.__name__,
            "maxProjectiles": self.maxProjectiles,
            "reloadTime": self.reloadTime,
            "reload": self.reload,
            "projectiles": self.projectiles,
            "world": self.world,
            "destructionWorld": self.destructionWorld,
        })
