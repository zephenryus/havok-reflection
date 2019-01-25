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
        self.sectionTag = struct.unpack('>c', infile.read(1))
        self.nullByte = struct.unpack('>c', infile.read(1))
        self.absoluteDataStart = struct.unpack('>i', infile.read(4))
        self.localFixupsOffset = struct.unpack('>i', infile.read(4))
        self.globalFixupsOffset = struct.unpack('>i', infile.read(4))
        self.virtualFixupsOffset = struct.unpack('>i', infile.read(4))
        self.exportsOffset = struct.unpack('>i', infile.read(4))
        self.importsOffset = struct.unpack('>i', infile.read(4))
        self.endOffset = struct.unpack('>i', infile.read(4))
        self.pad = struct.unpack('>i', infile.read(4))
