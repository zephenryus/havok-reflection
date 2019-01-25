class hkDocumentationAttribute(object):
    getDocsSectionTag: any

    def __init__(self, infile):
        self.getDocsSectionTag = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} getDocsSectionTag={getDocsSectionTag}>".format(**{
            "class_name": self.__class__.__name__,
            "getDocsSectionTag": self.getDocsSectionTag,
        })
