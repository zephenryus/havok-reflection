from .hkReferencedObject import hkReferencedObject


class hkRootLevelContainerNamedVariant(object):
    name: str
    className: str
    variant: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.className = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.variant = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} name=\"{name}\", className=\"{className}\", variant={variant}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "className": self.className,
            "variant": self.variant,
        })
