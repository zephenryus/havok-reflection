from .common import any


class hkaMeshBindingMapping(object):
    mapping: any

    def __init__(self, infile):
        self.mapping = any(infile)  # TYPE_ARRAY
