from .hkpCollidable import hkpCollidable
from .common import any


class hkpLinkedCollidable(hkpCollidable):
    collisionEntries: any

    def __init__(self, infile):
        self.collisionEntries = any(infile)  # TYPE_ARRAY
