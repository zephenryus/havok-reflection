class hkMemoryResourceHandleExternalLink(object):
    memberName: str
    externalId: str

    def __init__(self, infile):
        self.memberName = struct.unpack('>s', infile.read(0))
        self.externalId = struct.unpack('>s', infile.read(0))
