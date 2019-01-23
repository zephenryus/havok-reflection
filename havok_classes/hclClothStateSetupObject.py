from .hkReferencedObject import hkReferencedObject
from .hclOperatorSetupObject import hclOperatorSetupObject


class hclClothStateSetupObject(hkReferencedObject):
	name: any
	operatorSetupObjects: hclOperatorSetupObject
