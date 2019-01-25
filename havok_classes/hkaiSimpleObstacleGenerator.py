from .hkaiObstacleGenerator import hkaiObstacleGenerator
from .hkAabb import hkAabb


class hkaiSimpleObstacleGenerator(hkaiObstacleGenerator):
    localAabb: hkAabb

    def __init__(self, infile):
        self.localAabb = hkAabb(infile)  # TYPE_STRUCT
