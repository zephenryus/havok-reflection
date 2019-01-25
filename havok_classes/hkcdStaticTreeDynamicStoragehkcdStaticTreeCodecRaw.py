from .hkcdStaticTreeCodecRaw import hkcdStaticTreeCodecRaw


class hkcdStaticTreeDynamicStoragehkcdStaticTreeCodecRaw(object):
    nodes: hkcdStaticTreeCodecRaw

    def __init__(self, infile):
        self.nodes = hkcdStaticTreeCodecRaw(infile)  # TYPE_ARRAY
