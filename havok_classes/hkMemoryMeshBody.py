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

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_MATRIX4
        self.transformSet = hkIndexedTransformSet(infile)  # TYPE_POINTER
        self.shape = hkMeshShape(infile)  # TYPE_POINTER
        self.vertexBuffers = hkMeshVertexBuffer(infile)  # TYPE_ARRAY
        self.name = struct.unpack('>s', infile.read(0))
