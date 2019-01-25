from .hkpEntitySmallArraySerializeOverrideType import hkpEntitySmallArraySerializeOverrideType


class hkpEntityExtendedListeners(object):
    activationListeners: hkpEntitySmallArraySerializeOverrideType
    entityListeners: hkpEntitySmallArraySerializeOverrideType

    def __init__(self, infile):
        self.activationListeners = hkpEntitySmallArraySerializeOverrideType(infile)  # TYPE_STRUCT:TYPE_VOID
        self.entityListeners = hkpEntitySmallArraySerializeOverrideType(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} activationListeners={activationListeners}, entityListeners={entityListeners}>".format(**{
            "class_name": self.__class__.__name__,
            "activationListeners": self.activationListeners,
            "entityListeners": self.entityListeners,
        })
