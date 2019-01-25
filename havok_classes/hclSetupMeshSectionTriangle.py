import struct


class hclSetupMeshSectionTriangle(object):
    indices: int

    def __init__(self, infile):
        self.indices = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} indices={indices}>".format(**{
            "class_name": self.__class__.__name__,
            "indices": self.indices,
        })
