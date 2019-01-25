from .hkpEntitySmallArraySerializeOverrideType import hkpEntitySmallArraySerializeOverrideType


class hkpEntityExtendedListeners(object):
    activationListeners: hkpEntitySmallArraySerializeOverrideType
    entityListeners: hkpEntitySmallArraySerializeOverrideType

    def __init__(self, infile):
        self.activationListeners = hkpEntitySmallArraySerializeOverrideType(infile)  # TYPE_STRUCT
        self.entityListeners = hkpEntitySmallArraySerializeOverrideType(infile)  # TYPE_STRUCT
