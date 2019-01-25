from .hkReferencedObject import hkReferencedObject
from .hclOperatorSetupObject import hclOperatorSetupObject


class hclClothStateSetupObject(hkReferencedObject):
    name: str
    operatorSetupObjects: hclOperatorSetupObject

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.operatorSetupObjects = hclOperatorSetupObject(infile)  # TYPE_ARRAY
