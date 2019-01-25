from .hkaiSilhouetteMerger import hkaiSilhouetteMerger


class hkaiSimpleSilhouetteMerger(hkaiSilhouetteMerger):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
