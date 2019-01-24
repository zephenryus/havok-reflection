from .hkpRigidBody import hkpRigidBody
from .enums import Operation


class hkpTriggerVolumeEventInfo(object):
    sortValue: int
    body: hkpRigidBody
    operation: Operation
