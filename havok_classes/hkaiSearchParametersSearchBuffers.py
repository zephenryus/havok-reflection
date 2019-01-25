from .common import any


class hkaiSearchParametersSearchBuffers(object):
    openSetBuffer: any
    searchStateBuffer: any

    def __init__(self, infile):
        self.openSetBuffer = any(infile)  # TYPE_POINTER
        self.searchStateBuffer = any(infile)  # TYPE_POINTER
