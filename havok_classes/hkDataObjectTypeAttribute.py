class hkDataObjectTypeAttribute(object):
    typeName: str

    def __init__(self, infile):
        self.typeName = str(infile)  # TYPE_CSTRING:TYPE_VOID

    def __repr__(self):
        return "<{class_name} typeName=\"{typeName}\">".format(**{
            "class_name": self.__class__.__name__,
            "typeName": self.typeName,
        })
