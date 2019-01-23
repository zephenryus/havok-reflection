from .hkReferencedObject import hkReferencedObject


class hkxCamera(hkReferencedObject):
	from: any
	focus: any
	up: any
	fov: float
	far: float
	near: float
	leftHanded: bool
