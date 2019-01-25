from .hkAabb import hkAabb


class hkcdStaticTreeCodecRaw(object):
    aabb: hkAabb

    def __init__(self, infile):
        self.aabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} aabb={aabb}>".format(**{
            "class_name": self.__class__.__name__,
            "aabb": self.aabb,
        })
