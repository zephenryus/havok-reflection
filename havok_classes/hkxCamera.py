from .hkReferencedObject import hkReferencedObject
from .common import vector4


class hkxCamera(hkReferencedObject):
    from: vector4
    focus: vector4
    up: vector4
    fov: float
    far: float
    near: float
    leftHanded: bool
