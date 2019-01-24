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
