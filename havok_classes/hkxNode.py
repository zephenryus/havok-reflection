from .hkxAttributeHolder import hkxAttributeHolder
from .hkUuid import hkUuid
from .hkReferencedObject import hkReferencedObject
from .common import any
from .hkxNode import hkxNode
from .hkxNodeAnnotationData import hkxNodeAnnotationData


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
