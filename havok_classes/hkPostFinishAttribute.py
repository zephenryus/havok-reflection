class hkPostFinishAttribute(object):
    postFinishFunction: any

    def __init__(self, infile):
        self.postFinishFunction = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} postFinishFunction={postFinishFunction}>".format(**{
            "class_name": self.__class__.__name__,
            "postFinishFunction": self.postFinishFunction,
        })
