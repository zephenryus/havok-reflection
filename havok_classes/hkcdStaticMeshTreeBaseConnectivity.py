from typing import List
from .common import get_array
from .hkcdStaticMeshTreeBaseConnectivitySectionHeader import hkcdStaticMeshTreeBaseConnectivitySectionHeader


class hkcdStaticMeshTreeBaseConnectivity(object):
    headers: List[hkcdStaticMeshTreeBaseConnectivitySectionHeader]
    localLinks: List[int]
    globalLinks: List[int]

    def __init__(self, infile):
        self.headers = get_array(infile, hkcdStaticMeshTreeBaseConnectivitySectionHeader, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.localLinks = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.globalLinks = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32

    def __repr__(self):
        return "<{class_name} headers=[{headers}], localLinks=[{localLinks}], globalLinks=[{globalLinks}]>".format(**{
            "class_name": self.__class__.__name__,
            "headers": self.headers,
            "localLinks": self.localLinks,
            "globalLinks": self.globalLinks,
        })
