from .hkpAction import hkpAction
from .hkpEntity import hkpEntity


class hkpUnaryAction(hkpAction):
    entity: any

    def __init__(self, infile):
        self.entity = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} entity={entity}>".format(**{
            "class_name": self.__class__.__name__,
            "entity": self.entity,
        })
