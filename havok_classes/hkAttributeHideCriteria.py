from enum import Enum


class Types(Enum):
    NONE = 0
    MODELER_IS_MAX = 1
    MODELER_IS_MAYA = 2
    UI_SCHEME_IS_DESTRUCTION = 4
    UI_SCHEME_IS_DESTRUCTION_2012 = 8


class hkAttributeHideCriteria(object):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
