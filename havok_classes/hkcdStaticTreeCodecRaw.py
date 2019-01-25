from .hkAabb import hkAabb


class hkcdStaticTreeCodecRaw(object):
    aabb: hkAabb

    def __init__(self, infile):
        self.aabb = hkAabb(infile)  # TYPE_STRUCT
