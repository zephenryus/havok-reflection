from .hkReferencedObject import hkReferencedObject
from .hkxVertexBufferVertexData import hkxVertexBufferVertexData
from .hkxVertexDescription import hkxVertexDescription


class hkxVertexBuffer(hkReferencedObject):
    data: hkxVertexBufferVertexData
    desc: hkxVertexDescription

    def __init__(self, infile):
        self.data = hkxVertexBufferVertexData(infile)  # TYPE_STRUCT
        self.desc = hkxVertexDescription(infile)  # TYPE_STRUCT
