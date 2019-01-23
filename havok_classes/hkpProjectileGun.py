from .hkpFirstPersonGun import hkpFirstPersonGun


class hkpProjectileGun(hkpFirstPersonGun):
	maxProjectiles: int
	reloadTime: float
	reload: float
	projectiles: any
	world: any
	destructionWorld: any
