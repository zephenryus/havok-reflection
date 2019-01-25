class hkMemoryResourceHandleExternalLink(object):
    memberName: str
    externalId: str

    def __init__(self, infile):
        self.memberName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.externalId = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} memberName=\"{memberName}\", externalId=\"{externalId}\">".format(**{
            "class_name": self.__class__.__name__,
            "memberName": self.memberName,
            "externalId": self.externalId,
        })
