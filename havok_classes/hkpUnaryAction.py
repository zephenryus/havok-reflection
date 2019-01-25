from .hkpAction import hkpAction
from .hkpEntity import hkpEntity


class hkpUnaryAction(hkpAction):
    entity: hkpEntity

    def __init__(self, infile):
        self.entity = hkpEntity(infile)  # TYPE_POINTER
