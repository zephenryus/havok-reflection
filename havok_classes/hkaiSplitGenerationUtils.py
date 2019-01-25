from enum import Enum


class SplitAndGenerateOptions(Enum):
    SIMPLIFY_INDIVIDUALLY = 0
    SIMPLIFY_INDIVIDUALLY_BORDER_PRESERVE = 1
    SIMPLIFY_ALL_AT_ONCE = 2
    SIMPLIFY_TWO_PASS = 3


class SplitMethod(Enum):
    SPLIT_UNIFORM = 0
    SPLIT_ADAPTIVE = 1


class hkaiSplitGenerationUtils(object):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
