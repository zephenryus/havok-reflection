from .hkpShape import hkpShape
from enum import Enum
import struct
from .enums import CollectionType


class CollectionType(Enum):
    COLLECTION_LIST = 0
    COLLECTION_EXTENDED_MESH = 1
    COLLECTION_TRISAMPLED_HEIGHTFIELD = 2
    COLLECTION_USER = 3
    COLLECTION_SIMPLE_MESH = 4
    COLLECTION_MESH_SHAPE = 5
    COLLECTION_COMPRESSED_MESH = 6
    COLLECTION_MAX = 7


class hkpShapeCollection(hkpShape):
    disableWelding: bool
    collectionType: CollectionType

    def __init__(self, infile):
        self.disableWelding = struct.unpack('>?', infile.read(1))
        self.collectionType = CollectionType(infile)  # TYPE_ENUM
