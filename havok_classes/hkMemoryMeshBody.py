from .hkMeshBody import hkMeshBody
from .hkIndexedTransformSet import hkIndexedTransformSet
from .hkMeshShape import hkMeshShape
from typing import List
from .common import get_array
from .hkMeshVertexBuffer import hkMeshVertexBuffer


class hkMemoryMeshBody(hkMeshBody):
    transform: any
    transformSet: any
    shape: any
    vertexBuffers: List[hkMeshVertexBuffer]
    name: str

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_MATRIX4:TYPE_VOID
        self.transformSet = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.shape = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.vertexBuffers = get_array(infile, hkMeshVertexBuffer, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transform={transform}, transformSet={transformSet}, shape={shape}, vertexBuffers=[{vertexBuffers}], name=\"{name}\">".format(**{
            "class_name": self.__class__.__name__,
            "transform": self.transform,
            "transformSet": self.transformSet,
            "shape": self.shape,
            "vertexBuffers": self.vertexBuffers,
            "name": self.name,
        })
