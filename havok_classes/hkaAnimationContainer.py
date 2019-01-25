from .hkReferencedObject import hkReferencedObject
from .hkaSkeleton import hkaSkeleton
from .hkaAnimation import hkaAnimation
from .hkaAnimationBinding import hkaAnimationBinding
from .hkaBoneAttachment import hkaBoneAttachment
from .hkaMeshBinding import hkaMeshBinding


class hkaAnimationContainer(hkReferencedObject):
    skeletons: hkaSkeleton
    animations: hkaAnimation
    bindings: hkaAnimationBinding
    attachments: hkaBoneAttachment
    skins: hkaMeshBinding

    def __init__(self, infile):
        self.skeletons = hkaSkeleton(infile)  # TYPE_ARRAY
        self.animations = hkaAnimation(infile)  # TYPE_ARRAY
        self.bindings = hkaAnimationBinding(infile)  # TYPE_ARRAY
        self.attachments = hkaBoneAttachment(infile)  # TYPE_ARRAY
        self.skins = hkaMeshBinding(infile)  # TYPE_ARRAY
