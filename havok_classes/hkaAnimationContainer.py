from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkaSkeleton import hkaSkeleton
from .hkaAnimation import hkaAnimation
from .hkaAnimationBinding import hkaAnimationBinding
from .hkaBoneAttachment import hkaBoneAttachment
from .hkaMeshBinding import hkaMeshBinding


class hkaAnimationContainer(hkReferencedObject):
    skeletons: List[hkaSkeleton]
    animations: List[hkaAnimation]
    bindings: List[hkaAnimationBinding]
    attachments: List[hkaBoneAttachment]
    skins: List[hkaMeshBinding]

    def __init__(self, infile):
        self.skeletons = get_array(infile, hkaSkeleton, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.animations = get_array(infile, hkaAnimation, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.bindings = get_array(infile, hkaAnimationBinding, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.attachments = get_array(infile, hkaBoneAttachment, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.skins = get_array(infile, hkaMeshBinding, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} skeletons=[{skeletons}], animations=[{animations}], bindings=[{bindings}], attachments=[{attachments}], skins=[{skins}]>".format(**{
            "class_name": self.__class__.__name__,
            "skeletons": self.skeletons,
            "animations": self.animations,
            "bindings": self.bindings,
            "attachments": self.attachments,
            "skins": self.skins,
        })
