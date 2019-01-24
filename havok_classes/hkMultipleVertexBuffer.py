from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkVertexFormat import hkVertexFormat
from .hkMultipleVertexBufferLockedElement import hkMultipleVertexBufferLockedElement
from .hkMemoryMeshVertexBuffer import hkMemoryMeshVertexBuffer
from .hkMultipleVertexBufferElementInfo import hkMultipleVertexBufferElementInfo
from .hkMultipleVertexBufferVertexBufferInfo import hkMultipleVertexBufferVertexBufferInfo


class hkMultipleVertexBuffer(hkMeshVertexBuffer):
    vertexFormat: hkVertexFormat
    lockedElements: hkMultipleVertexBufferLockedElement
    lockedBuffer: hkMemoryMeshVertexBuffer
    elementInfos: hkMultipleVertexBufferElementInfo
    vertexBufferInfos: hkMultipleVertexBufferVertexBufferInfo
    numVertices: int
    isLocked: bool
    updateCount: int
    writeLock: bool
    isSharable: bool
    constructionComplete: bool
