from .hkpCollidable import hkpCollidable


class hkpSimpleShapePhantomCollisionDetail(object):
    collidable: any

    def __init__(self, infile):
        self.collidable = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} collidable={collidable}>".format(**{
            "class_name": self.__class__.__name__,
            "collidable": self.collidable,
        })
