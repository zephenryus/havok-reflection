class hkaiSearchParametersSearchBuffers(object):
    openSetBuffer: any
    searchStateBuffer: any

    def __init__(self, infile):
        self.openSetBuffer = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.searchStateBuffer = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} openSetBuffer={openSetBuffer}, searchStateBuffer={searchStateBuffer}>".format(**{
            "class_name": self.__class__.__name__,
            "openSetBuffer": self.openSetBuffer,
            "searchStateBuffer": self.searchStateBuffer,
        })
