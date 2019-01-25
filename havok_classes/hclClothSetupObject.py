from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hclBufferSetupObject import hclBufferSetupObject
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .hclSimClothSetupObject import hclSimClothSetupObject
from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclClothStateSetupObject import hclClothStateSetupObject


class hclClothSetupObject(hkReferencedObject):
    name: str
    bufferSetupObjects: List[hclBufferSetupObject]
    transformSetSetupObjects: List[hclTransformSetSetupObject]
    simClothSetupObjects: List[hclSimClothSetupObject]
    operatorSetupObjects: List[hclOperatorSetupObject]
    clothStateSetupObjects: List[hclClothStateSetupObject]

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.bufferSetupObjects = get_array(infile, hclBufferSetupObject, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.transformSetSetupObjects = get_array(infile, hclTransformSetSetupObject, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.simClothSetupObjects = get_array(infile, hclSimClothSetupObject, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.operatorSetupObjects = get_array(infile, hclOperatorSetupObject, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.clothStateSetupObjects = get_array(infile, hclClothStateSetupObject, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} name=\"{name}\", bufferSetupObjects=[{bufferSetupObjects}], transformSetSetupObjects=[{transformSetSetupObjects}], simClothSetupObjects=[{simClothSetupObjects}], operatorSetupObjects=[{operatorSetupObjects}], clothStateSetupObjects=[{clothStateSetupObjects}]>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "bufferSetupObjects": self.bufferSetupObjects,
            "transformSetSetupObjects": self.transformSetSetupObjects,
            "simClothSetupObjects": self.simClothSetupObjects,
            "operatorSetupObjects": self.operatorSetupObjects,
            "clothStateSetupObjects": self.clothStateSetupObjects,
        })
