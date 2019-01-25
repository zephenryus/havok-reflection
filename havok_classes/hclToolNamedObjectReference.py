import struct


class hclToolNamedObjectReference(object):
    pluginName: str
    objectName: str
    hash: int

    def __init__(self, infile):
        self.pluginName = struct.unpack('>s', infile.read(0))
        self.objectName = struct.unpack('>s', infile.read(0))
        self.hash = struct.unpack('>I', infile.read(4))
