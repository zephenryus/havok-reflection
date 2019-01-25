from .hkxAttributeHolder import hkxAttributeHolder
from .hkUuid import hkUuid
from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkxNode import hkxNode
from .hkxNodeAnnotationData import hkxNodeAnnotationData
import struct


class hkxNode(hkxAttributeHolder):
    name: str
    uuid: hkUuid
    object: any
    keyFrames: List[any]
    children: List[hkxNode]
    annotations: List[hkxNodeAnnotationData]
    linearKeyFrameHints: List[float]
    userProperties: str
    selected: bool
    bone: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.uuid = hkUuid(infile)  # TYPE_STRUCT:TYPE_VOID
        self.object = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.keyFrames = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_MATRIX4
        self.children = get_array(infile, hkxNode, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.annotations = get_array(infile, hkxNodeAnnotationData, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.linearKeyFrameHints = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.userProperties = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.selected = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.bone = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", uuid={uuid}, object={object}, keyFrames=[{keyFrames}], children=[{children}], annotations=[{annotations}], linearKeyFrameHints=[{linearKeyFrameHints}], userProperties=\"{userProperties}\", selected={selected}, bone={bone}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "uuid": self.uuid,
            "object": self.object,
            "keyFrames": self.keyFrames,
            "children": self.children,
            "annotations": self.annotations,
            "linearKeyFrameHints": self.linearKeyFrameHints,
            "userProperties": self.userProperties,
            "selected": self.selected,
            "bone": self.bone,
        })
