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
