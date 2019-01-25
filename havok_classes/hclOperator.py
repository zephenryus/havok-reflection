from .hkReferencedObject import hkReferencedObject


class hclOperator(hkReferencedObject):
    name: str
    type: enumerate

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.type = enumerate(infile)  # TYPE_ENUM
