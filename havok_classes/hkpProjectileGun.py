from .hkpFirstPersonGun import hkpFirstPersonGun
from .common import any


class hkpProjectileGun(hkpFirstPersonGun):
    maxProjectiles: int
    reloadTime: float
    reload: float
    projectiles: any
    world: any
    destructionWorld: any
