from .hkReferencedObject import hkReferencedObject


class hkWorldMemoryAvailableWatchDog(hkReferencedObject):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
