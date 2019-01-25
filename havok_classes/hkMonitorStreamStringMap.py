from .hkMonitorStreamStringMapStringMap import hkMonitorStreamStringMapStringMap


class hkMonitorStreamStringMap(object):
    map: hkMonitorStreamStringMapStringMap

    def __init__(self, infile):
        self.map = hkMonitorStreamStringMapStringMap(infile)  # TYPE_ARRAY
