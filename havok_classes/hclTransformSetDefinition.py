from .hkReferencedObject import hkReferencedObject


class hclTransformSetDefinition(hkReferencedObject):
    name: str
    type: int
    numTransforms: int
