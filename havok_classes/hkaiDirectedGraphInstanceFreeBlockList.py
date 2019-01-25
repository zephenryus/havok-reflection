from .common import any


class hkaiDirectedGraphInstanceFreeBlockList(object):
    blocks: any

    def __init__(self, infile):
        self.blocks = any(infile)  # TYPE_ARRAY
