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
        self.disableWelding = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.collectionType = CollectionType(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} disableWelding={disableWelding}, collectionType={collectionType}>".format(**{
            "class_name": self.__class__.__name__,
            "disableWelding": self.disableWelding,
            "collectionType": self.collectionType,
        })
