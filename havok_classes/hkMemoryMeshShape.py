from .hkMeshShape import hkMeshShape
from .hkMemoryMeshShapeSection import hkMemoryMeshShapeSection
from .common import any


class hkMemoryMeshShape(hkMeshShape):
    sections: hkMemoryMeshShapeSection
    indices16: any
    indices32: any
    name: str
