from .hkpMeshMaterial import hkpMeshMaterial


class hkpNamedMeshMaterial(hkpMeshMaterial):
    name: str

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
