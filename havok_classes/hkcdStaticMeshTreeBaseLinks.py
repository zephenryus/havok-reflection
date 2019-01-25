from .hkcdStaticMeshTreeBaseEdge import hkcdStaticMeshTreeBaseEdge


class hkcdStaticMeshTreeBaseLinks(object):
    links: hkcdStaticMeshTreeBaseEdge

    def __init__(self, infile):
        self.links = hkcdStaticMeshTreeBaseEdge(infile)  # TYPE_STRUCT
