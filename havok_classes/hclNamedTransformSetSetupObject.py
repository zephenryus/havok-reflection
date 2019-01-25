from .hclTransformSetSetupObject import hclTransformSetSetupObject


class hclNamedTransformSetSetupObject(hclTransformSetSetupObject):
    name: str
    skelName: str
    transformSet: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.skelName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.transformSet = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", skelName=\"{skelName}\", transformSet={transformSet}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "skelName": self.skelName,
            "transformSet": self.transformSet,
        })
