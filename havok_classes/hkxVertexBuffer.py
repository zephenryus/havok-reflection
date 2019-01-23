from .hkReferencedObject import hkReferencedObject
from .hkxVertexBufferVertexData import hkxVertexBufferVertexData
from .hkxVertexDescription import hkxVertexDescription


class hkxVertexBuffer(hkReferencedObject):
	data: hkxVertexBufferVertexData
	desc: hkxVertexDescription
