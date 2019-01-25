class hkDataObjectTypeAttribute(object):
    typeName: str

    def __init__(self, infile):
        self.typeName = str(infile)  # TYPE_CSTRING
