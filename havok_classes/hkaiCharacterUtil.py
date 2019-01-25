from enum import Enum


class CallbackType(Enum):
    CALLBACK_PATH_SUCCEEDED = 0
    CALLBACK_PATH_FAILED_INVALID_START = 1
    CALLBACK_PATH_FAILED_INVALID_GOAL = 2
    CALLBACK_PATH_FAILED_INVALID_UNREACHABLE = 3
    CALLBACK_PATH_NOT_READY = 4


class hkaiCharacterUtil(object):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
