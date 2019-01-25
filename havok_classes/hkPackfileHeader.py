import struct


class hkPackfileHeader(object):
    magic: int
    userTag: int
    fileVersion: int
    layoutRules: int
    numSections: int
    contentsSectionIndex: int
    contentsSectionOffset: int
    contentsClassNameSectionIndex: int
    contentsClassNameSectionOffset: int
    contentsVersion: str
    flags: int
    maxpredicate: int
    predicateArraySizePlusPadding: int

    def __init__(self, infile):
        self.magic = struct.unpack('>i', infile.read(4))
        self.userTag = struct.unpack('>i', infile.read(4))
        self.fileVersion = struct.unpack('>i', infile.read(4))
        self.layoutRules = struct.unpack('>B', infile.read(1))
        self.numSections = struct.unpack('>i', infile.read(4))
        self.contentsSectionIndex = struct.unpack('>i', infile.read(4))
        self.contentsSectionOffset = struct.unpack('>i', infile.read(4))
        self.contentsClassNameSectionIndex = struct.unpack('>i', infile.read(4))
        self.contentsClassNameSectionOffset = struct.unpack('>i', infile.read(4))
        self.contentsVersion = struct.unpack('>c', infile.read(1))
        self.flags = struct.unpack('>i', infile.read(4))
        self.maxpredicate = struct.unpack('>H', infile.read(2))
        self.predicateArraySizePlusPadding = struct.unpack('>H', infile.read(2))
