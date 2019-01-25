from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hclOperatorSetupObject import hclOperatorSetupObject


class hclClothStateSetupObject(hkReferencedObject):
    name: str
    operatorSetupObjects: List[hclOperatorSetupObject]

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.operatorSetupObjects = get_array(infile, hclOperatorSetupObject, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} name=\"{name}\", operatorSetupObjects=[{operatorSetupObjects}]>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "operatorSetupObjects": self.operatorSetupObjects,
        })
