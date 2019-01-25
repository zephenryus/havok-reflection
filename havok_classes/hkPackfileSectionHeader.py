import struct


class hkPackfileSectionHeader(object):
    sectionTag: str
    nullByte: str
    absoluteDataStart: int
    localFixupsOffset: int
    globalFixupsOffset: int
    virtualFixupsOffset: int
    exportsOffset: int
    importsOffset: int
    endOffset: int
    pad: int

    def __init__(self, infile):
        self.sectionTag = struct.unpack('>c', infile.read(1))  # TYPE_CHAR:TYPE_VOID
        self.nullByte = struct.unpack('>c', infile.read(1))  # TYPE_CHAR:TYPE_VOID
        self.absoluteDataStart = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.localFixupsOffset = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.globalFixupsOffset = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.virtualFixupsOffset = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.exportsOffset = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.importsOffset = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.endOffset = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.pad = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} sectionTag=\"{sectionTag}\", nullByte=\"{nullByte}\", absoluteDataStart={absoluteDataStart}, localFixupsOffset={localFixupsOffset}, globalFixupsOffset={globalFixupsOffset}, virtualFixupsOffset={virtualFixupsOffset}, exportsOffset={exportsOffset}, importsOffset={importsOffset}, endOffset={endOffset}, pad={pad}>".format(**{
            "class_name": self.__class__.__name__,
            "sectionTag": self.sectionTag,
            "nullByte": self.nullByte,
            "absoluteDataStart": self.absoluteDataStart,
            "localFixupsOffset": self.localFixupsOffset,
            "globalFixupsOffset": self.globalFixupsOffset,
            "virtualFixupsOffset": self.virtualFixupsOffset,
            "exportsOffset": self.exportsOffset,
            "importsOffset": self.importsOffset,
            "endOffset": self.endOffset,
            "pad": self.pad,
        })
