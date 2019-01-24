from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .common import any


class hclNamedTransformSetSetupObject(hclTransformSetSetupObject):
    name: str
    skelName: str
    transformSet: any
