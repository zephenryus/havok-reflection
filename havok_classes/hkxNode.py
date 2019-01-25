from .hkxAttributeHolder import hkxAttributeHolder
from .hkUuid import hkUuid
from .hkReferencedObject import hkReferencedObject
from .common import any
from .hkxNode import hkxNode
from .hkxNodeAnnotationData import hkxNodeAnnotationData
import struct


class hkxNode(hkxAttributeHolder):
    name: str
    uuid: hkUuid
    object: hkReferencedObject
    keyFrames: any
    children: hkxNode
    annotations: hkxNodeAnnotationData
    linearKeyFrameHints: any
    userProperties: str
    selected: bool
    bone: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.uuid = hkUuid(infile)  # TYPE_STRUCT
        self.object = hkReferencedObject(infile)  # TYPE_POINTER
        self.keyFrames = any(infile)  # TYPE_ARRAY
        self.children = hkxNode(infile)  # TYPE_ARRAY
        self.annotations = hkxNodeAnnotationData(infile)  # TYPE_ARRAY
        self.linearKeyFrameHints = any(infile)  # TYPE_ARRAY
        self.userProperties = struct.unpack('>s', infile.read(0))
        self.selected = struct.unpack('>?', infile.read(1))
        self.bone = struct.unpack('>?', infile.read(1))
