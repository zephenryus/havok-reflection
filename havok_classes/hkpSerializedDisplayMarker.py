from .hkReferencedObject import hkReferencedObject


class hkpSerializedDisplayMarker(hkReferencedObject):
    transform: any

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transform={transform}>".format(**{
            "class_name": self.__class__.__name__,
            "transform": self.transform,
        })
