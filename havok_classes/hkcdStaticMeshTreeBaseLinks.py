from .hkcdStaticMeshTreeBaseEdge import hkcdStaticMeshTreeBaseEdge


class hkcdStaticMeshTreeBaseLinks(object):
    links: hkcdStaticMeshTreeBaseEdge

    def __init__(self, infile):
        self.links = hkcdStaticMeshTreeBaseEdge(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} links={links}>".format(**{
            "class_name": self.__class__.__name__,
            "links": self.links,
        })
