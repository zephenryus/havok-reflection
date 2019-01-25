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
        self.magic = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.userTag = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.fileVersion = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.layoutRules = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.numSections = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.contentsSectionIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.contentsSectionOffset = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.contentsClassNameSectionIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.contentsClassNameSectionOffset = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.contentsVersion = struct.unpack('>c', infile.read(1))  # TYPE_CHAR:TYPE_VOID
        self.flags = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxpredicate = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.predicateArraySizePlusPadding = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} magic={magic}, userTag={userTag}, fileVersion={fileVersion}, layoutRules={layoutRules}, numSections={numSections}, contentsSectionIndex={contentsSectionIndex}, contentsSectionOffset={contentsSectionOffset}, contentsClassNameSectionIndex={contentsClassNameSectionIndex}, contentsClassNameSectionOffset={contentsClassNameSectionOffset}, contentsVersion=\"{contentsVersion}\", flags={flags}, maxpredicate={maxpredicate}, predicateArraySizePlusPadding={predicateArraySizePlusPadding}>".format(**{
            "class_name": self.__class__.__name__,
            "magic": self.magic,
            "userTag": self.userTag,
            "fileVersion": self.fileVersion,
            "layoutRules": self.layoutRules,
            "numSections": self.numSections,
            "contentsSectionIndex": self.contentsSectionIndex,
            "contentsSectionOffset": self.contentsSectionOffset,
            "contentsClassNameSectionIndex": self.contentsClassNameSectionIndex,
            "contentsClassNameSectionOffset": self.contentsClassNameSectionOffset,
            "contentsVersion": self.contentsVersion,
            "flags": self.flags,
            "maxpredicate": self.maxpredicate,
            "predicateArraySizePlusPadding": self.predicateArraySizePlusPadding,
        })
