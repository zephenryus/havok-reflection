from .hkxAttributeHolder import hkxAttributeHolder


class hkxMeshUserChannelInfo(hkxAttributeHolder):
    name: str
    className: str

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.className = struct.unpack('>s', infile.read(0))
