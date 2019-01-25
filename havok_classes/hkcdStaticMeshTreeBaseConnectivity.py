from .hkcdStaticMeshTreeBaseConnectivitySectionHeader import hkcdStaticMeshTreeBaseConnectivitySectionHeader
from .common import any


class hkcdStaticMeshTreeBaseConnectivity(object):
    headers: hkcdStaticMeshTreeBaseConnectivitySectionHeader
    localLinks: any
    globalLinks: any

    def __init__(self, infile):
        self.headers = hkcdStaticMeshTreeBaseConnectivitySectionHeader(infile)  # TYPE_ARRAY
        self.localLinks = any(infile)  # TYPE_ARRAY
        self.globalLinks = any(infile)  # TYPE_ARRAY
