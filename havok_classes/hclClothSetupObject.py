from .hkReferencedObject import hkReferencedObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .hclSimClothSetupObject import hclSimClothSetupObject
from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclClothStateSetupObject import hclClothStateSetupObject


class hclClothSetupObject(hkReferencedObject):
    name: str
    bufferSetupObjects: hclBufferSetupObject
    transformSetSetupObjects: hclTransformSetSetupObject
    simClothSetupObjects: hclSimClothSetupObject
    operatorSetupObjects: hclOperatorSetupObject
    clothStateSetupObjects: hclClothStateSetupObject

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.bufferSetupObjects = hclBufferSetupObject(infile)  # TYPE_ARRAY
        self.transformSetSetupObjects = hclTransformSetSetupObject(infile)  # TYPE_ARRAY
        self.simClothSetupObjects = hclSimClothSetupObject(infile)  # TYPE_ARRAY
        self.operatorSetupObjects = hclOperatorSetupObject(infile)  # TYPE_ARRAY
        self.clothStateSetupObjects = hclClothStateSetupObject(infile)  # TYPE_ARRAY
