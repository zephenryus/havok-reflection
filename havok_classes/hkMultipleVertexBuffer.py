from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkVertexFormat import hkVertexFormat
from typing import List
from .common import get_array
from .hkMultipleVertexBufferLockedElement import hkMultipleVertexBufferLockedElement
from .hkMemoryMeshVertexBuffer import hkMemoryMeshVertexBuffer
from .hkMultipleVertexBufferElementInfo import hkMultipleVertexBufferElementInfo
from .hkMultipleVertexBufferVertexBufferInfo import hkMultipleVertexBufferVertexBufferInfo
import struct


class hkMultipleVertexBuffer(hkMeshVertexBuffer):
    vertexFormat: hkVertexFormat
    lockedElements: List[hkMultipleVertexBufferLockedElement]
    lockedBuffer: any
    elementInfos: List[hkMultipleVertexBufferElementInfo]
    vertexBufferInfos: List[hkMultipleVertexBufferVertexBufferInfo]
    numVertices: int
    isLocked: bool
    updateCount: int
    writeLock: bool
    isSharable: bool
    constructionComplete: bool

    def __init__(self, infile):
        self.vertexFormat = hkVertexFormat(infile)  # TYPE_STRUCT:TYPE_VOID
        self.lockedElements = get_array(infile, hkMultipleVertexBufferLockedElement, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.lockedBuffer = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.elementInfos = get_array(infile, hkMultipleVertexBufferElementInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.vertexBufferInfos = get_array(infile, hkMultipleVertexBufferVertexBufferInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.numVertices = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.isLocked = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.updateCount = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.writeLock = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.isSharable = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.constructionComplete = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexFormat={vertexFormat}, lockedElements=[{lockedElements}], lockedBuffer={lockedBuffer}, elementInfos=[{elementInfos}], vertexBufferInfos=[{vertexBufferInfos}], numVertices={numVertices}, isLocked={isLocked}, updateCount={updateCount}, writeLock={writeLock}, isSharable={isSharable}, constructionComplete={constructionComplete}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexFormat": self.vertexFormat,
            "lockedElements": self.lockedElements,
            "lockedBuffer": self.lockedBuffer,
            "elementInfos": self.elementInfos,
            "vertexBufferInfos": self.vertexBufferInfos,
            "numVertices": self.numVertices,
            "isLocked": self.isLocked,
            "updateCount": self.updateCount,
            "writeLock": self.writeLock,
            "isSharable": self.isSharable,
            "constructionComplete": self.constructionComplete,
        })
