class hkCustomAttributesAttribute(object):
    name: str
    value: any

    def __init__(self, infile):
        self.name = str(infile)  # TYPE_CSTRING:TYPE_VOID
        self.value = any(infile)  # TYPE_VARIANT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", value={value}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "value": self.value,
        })
