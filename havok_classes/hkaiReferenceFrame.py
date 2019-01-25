import struct


class hkaiReferenceFrame(object):
    transform: any
    linearVelocity: vector4
    angularVelocity: vector4

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.linearVelocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.angularVelocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transform={transform}, linearVelocity={linearVelocity}, angularVelocity={angularVelocity}>".format(**{
            "class_name": self.__class__.__name__,
            "transform": self.transform,
            "linearVelocity": self.linearVelocity,
            "angularVelocity": self.angularVelocity,
        })
