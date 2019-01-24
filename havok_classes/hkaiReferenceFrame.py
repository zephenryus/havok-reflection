from .common import any, vector4


class hkaiReferenceFrame(object):
    transform: any
    linearVelocity: vector4
    angularVelocity: vector4
