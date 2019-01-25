import struct
from .enums import Types


class hkUiAttribute(object):
    visible: bool
    editable: bool
    hideCriteria: Types
    label: str
    group: str
    hideBaseClassMembers: str
    endGroup: bool
    endGroup2: bool
    advanced: bool

    def __init__(self, infile):
        self.visible = struct.unpack('>?', infile.read(1))
        self.editable = struct.unpack('>?', infile.read(1))
        self.hideCriteria = Types(infile)  # TYPE_ENUM
        self.label = str(infile)  # TYPE_CSTRING
        self.group = str(infile)  # TYPE_CSTRING
        self.hideBaseClassMembers = str(infile)  # TYPE_CSTRING
        self.endGroup = struct.unpack('>?', infile.read(1))
        self.endGroup2 = struct.unpack('>?', infile.read(1))
        self.advanced = struct.unpack('>?', infile.read(1))
