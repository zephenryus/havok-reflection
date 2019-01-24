from .hkAabb import hkAabb
from .common import vector4, any


class hkcdAdf(object):
    accuracy: float
    domain: hkAabb
    origin: vector4
    scale: vector4
    range: float
    nodes: any
    voxels: any
