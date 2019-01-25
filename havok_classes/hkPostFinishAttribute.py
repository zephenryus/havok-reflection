from .common import any


class hkPostFinishAttribute(object):
    postFinishFunction: any

    def __init__(self, infile):
        self.postFinishFunction = any(infile)  # TYPE_POINTER
