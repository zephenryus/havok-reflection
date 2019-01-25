from .hkMeshShape import hkMeshShape
from .hkMemoryMeshShapeSection import hkMemoryMeshShapeSection
from .common import any


class hkMemoryMeshShape(hkMeshShape):
    sections: hkMemoryMeshShapeSection
    indices16: any
    indices32: any
    name: str

    def __init__(self, infile):
        self.sections = hkMemoryMeshShapeSection(infile)  # TYPE_ARRAY
        self.indices16 = any(infile)  # TYPE_ARRAY
        self.indices32 = any(infile)  # TYPE_ARRAY
        self.name = struct.unpack('>s', infile.read(0))
