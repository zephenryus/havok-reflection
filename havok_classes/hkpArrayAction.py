from .hkpAction import hkpAction
from .hkpEntity import hkpEntity


class hkpArrayAction(hkpAction):
    entities: hkpEntity

    def __init__(self, infile):
        self.entities = hkpEntity(infile)  # TYPE_ARRAY
