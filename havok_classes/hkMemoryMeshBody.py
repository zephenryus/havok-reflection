from .hkMeshBody import hkMeshBody
from .common import any
from .hkIndexedTransformSet import hkIndexedTransformSet
from .hkMeshShape import hkMeshShape
from .hkMeshVertexBuffer import hkMeshVertexBuffer


class hkMemoryMeshBody(hkMeshBody):
    transform: any
    transformSet: hkIndexedTransformSet
    shape: hkMeshShape
    vertexBuffers: hkMeshVertexBuffer
    name: str
