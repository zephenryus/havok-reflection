from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .common import any


class hclNamedTransformSetSetupObject(hclTransformSetSetupObject):
    name: str
    skelName: str
    transformSet: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.skelName = struct.unpack('>s', infile.read(0))
        self.transformSet = any(infile)  # TYPE_POINTER
