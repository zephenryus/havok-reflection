from .common import any


class hkDocumentationAttribute(object):
    getDocsSectionTag: any

    def __init__(self, infile):
        self.getDocsSectionTag = any(infile)  # TYPE_POINTER
