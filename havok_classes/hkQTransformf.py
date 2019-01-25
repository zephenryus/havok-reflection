import struct


class hkQTransformf(object):
    rotation: any
    translation: vector4

    def __init__(self, infile):
        self.rotation = any(infile)  # TYPE_QUATERNION:TYPE_VOID
        self.translation = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rotation={rotation}, translation={translation}>".format(**{
            "class_name": self.__class__.__name__,
            "rotation": self.rotation,
            "translation": self.translation,
        })
