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
        self.visible = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.editable = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.hideCriteria = Types(infile)  # TYPE_ENUM:TYPE_INT8
        self.label = str(infile)  # TYPE_CSTRING:TYPE_VOID
        self.group = str(infile)  # TYPE_CSTRING:TYPE_VOID
        self.hideBaseClassMembers = str(infile)  # TYPE_CSTRING:TYPE_VOID
        self.endGroup = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.endGroup2 = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.advanced = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} visible={visible}, editable={editable}, hideCriteria={hideCriteria}, label=\"{label}\", group=\"{group}\", hideBaseClassMembers=\"{hideBaseClassMembers}\", endGroup={endGroup}, endGroup2={endGroup2}, advanced={advanced}>".format(**{
            "class_name": self.__class__.__name__,
            "visible": self.visible,
            "editable": self.editable,
            "hideCriteria": self.hideCriteria,
            "label": self.label,
            "group": self.group,
            "hideBaseClassMembers": self.hideBaseClassMembers,
            "endGroup": self.endGroup,
            "endGroup2": self.endGroup2,
            "advanced": self.advanced,
        })
