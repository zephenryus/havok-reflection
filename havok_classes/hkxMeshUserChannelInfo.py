from .hkxAttributeHolder import hkxAttributeHolder


class hkxMeshUserChannelInfo(hkxAttributeHolder):
    name: str
    className: str

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.className = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", className=\"{className}\">".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "className": self.className,
        })
