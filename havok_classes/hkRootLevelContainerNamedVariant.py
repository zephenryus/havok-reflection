from .hkReferencedObject import hkReferencedObject


class hkRootLevelContainerNamedVariant(object):
    name: str
    className: str
    variant: hkReferencedObject

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.className = struct.unpack('>s', infile.read(0))
        self.variant = hkReferencedObject(infile)  # TYPE_POINTER
