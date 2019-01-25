from .hkReferencedObject import hkReferencedObject


class hclShape(hkReferencedObject):
    type: enumerate

    def __init__(self, infile):
        self.type = enumerate(infile)  # TYPE_ENUM:TYPE_INT32

    def __repr__(self):
        return "<{class_name} type={type}>".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
        })
