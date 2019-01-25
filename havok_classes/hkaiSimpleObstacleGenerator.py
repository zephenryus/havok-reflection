from .hkaiObstacleGenerator import hkaiObstacleGenerator
from .hkAabb import hkAabb


class hkaiSimpleObstacleGenerator(hkaiObstacleGenerator):
    localAabb: hkAabb

    def __init__(self, infile):
        self.localAabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} localAabb={localAabb}>".format(**{
            "class_name": self.__class__.__name__,
            "localAabb": self.localAabb,
        })
