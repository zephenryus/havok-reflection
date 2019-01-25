import struct


class hclToolNamedObjectReference(object):
    pluginName: str
    objectName: str
    hash: int

    def __init__(self, infile):
        self.pluginName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.objectName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.hash = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} pluginName=\"{pluginName}\", objectName=\"{objectName}\", hash={hash}>".format(**{
            "class_name": self.__class__.__name__,
            "pluginName": self.pluginName,
            "objectName": self.objectName,
            "hash": self.hash,
        })
