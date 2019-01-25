class hkxEnvironmentVariable(object):
    name: str
    value: str

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.value = struct.unpack('>s', infile.read(0))
