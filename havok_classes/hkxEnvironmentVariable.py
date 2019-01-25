class hkxEnvironmentVariable(object):
    name: str
    value: str

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.value = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", value=\"{value}\">".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "value": self.value,
        })
