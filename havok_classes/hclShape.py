from .hkReferencedObject import hkReferencedObject


class hclShape(hkReferencedObject):
    type: enumerate

    def __init__(self, infile):
        self.type = enumerate(infile)  # TYPE_ENUM
