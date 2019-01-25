from .hkReferencedObject import hkReferencedObject
import struct


class hkaBoneAttachment(hkReferencedObject):
    originalSkeletonName: str
    boneFromAttachment: any
    attachment: any
    name: str
    boneIndex: int

    def __init__(self, infile):
        self.originalSkeletonName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.boneFromAttachment = any(infile)  # TYPE_MATRIX4:TYPE_VOID
        self.attachment = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.boneIndex = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} originalSkeletonName=\"{originalSkeletonName}\", boneFromAttachment={boneFromAttachment}, attachment={attachment}, name=\"{name}\", boneIndex={boneIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "originalSkeletonName": self.originalSkeletonName,
            "boneFromAttachment": self.boneFromAttachment,
            "attachment": self.attachment,
            "name": self.name,
            "boneIndex": self.boneIndex,
        })
