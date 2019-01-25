from .hkpFirstPersonGun import hkpFirstPersonGun
import struct
from .common import any


class hkpProjectileGun(hkpFirstPersonGun):
    maxProjectiles: int
    reloadTime: float
    reload: float
    projectiles: any
    world: any
    destructionWorld: any

    def __init__(self, infile):
        self.maxProjectiles = struct.unpack('>i', infile.read(4))
        self.reloadTime = struct.unpack('>f', infile.read(4))
        self.reload = struct.unpack('>f', infile.read(4))
        self.projectiles = any(infile)  # TYPE_ARRAY
        self.world = any(infile)  # TYPE_POINTER
        self.destructionWorld = any(infile)  # TYPE_POINTER
