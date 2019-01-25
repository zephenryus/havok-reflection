from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkVertexFormat import hkVertexFormat
from .hkMultipleVertexBufferLockedElement import hkMultipleVertexBufferLockedElement
from .hkMemoryMeshVertexBuffer import hkMemoryMeshVertexBuffer
from .hkMultipleVertexBufferElementInfo import hkMultipleVertexBufferElementInfo
from .hkMultipleVertexBufferVertexBufferInfo import hkMultipleVertexBufferVertexBufferInfo
import struct


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

    def __init__(self, infile):
        self.vertexFormat = hkVertexFormat(infile)  # TYPE_STRUCT
        self.lockedElements = hkMultipleVertexBufferLockedElement(infile)  # TYPE_ARRAY
        self.lockedBuffer = hkMemoryMeshVertexBuffer(infile)  # TYPE_POINTER
        self.elementInfos = hkMultipleVertexBufferElementInfo(infile)  # TYPE_ARRAY
        self.vertexBufferInfos = hkMultipleVertexBufferVertexBufferInfo(infile)  # TYPE_ARRAY
        self.numVertices = struct.unpack('>i', infile.read(4))
        self.isLocked = struct.unpack('>?', infile.read(1))
        self.updateCount = struct.unpack('>I', infile.read(4))
        self.writeLock = struct.unpack('>?', infile.read(1))
        self.isSharable = struct.unpack('>?', infile.read(1))
        self.constructionComplete = struct.unpack('>?', infile.read(1))
