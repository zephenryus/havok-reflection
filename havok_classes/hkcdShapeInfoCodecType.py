from enum import Enum


class ShapeInfoCodecTypeEnum(Enum):
    NULL_CODEC = 0
    UFM358 = 1
    MAX_NUM_CODECS = 16


class hkcdShapeInfoCodecType(object):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
