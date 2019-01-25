from .hkpRigidBody import hkpRigidBody


class hkpSerializedDisplayRbTransformsDisplayTransformPair(object):
    rb: any
    localToDisplay: any

    def __init__(self, infile):
        self.rb = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.localToDisplay = any(infile)  # TYPE_TRANSFORM:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rb={rb}, localToDisplay={localToDisplay}>".format(**{
            "class_name": self.__class__.__name__,
            "rb": self.rb,
            "localToDisplay": self.localToDisplay,
        })
