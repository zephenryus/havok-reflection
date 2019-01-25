from .hkpCollidable import hkpCollidable


class hkpSimpleShapePhantomCollisionDetail(object):
    collidable: hkpCollidable

    def __init__(self, infile):
        self.collidable = hkpCollidable(infile)  # TYPE_POINTER
