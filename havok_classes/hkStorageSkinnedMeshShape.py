from .hkSkinnedMeshShape import hkSkinnedMeshShape
from .common import any
from .hkSkinnedMeshShapeBoneSet import hkSkinnedMeshShapeBoneSet
from .hkSkinnedMeshShapeBoneSection import hkSkinnedMeshShapeBoneSection
from .hkSkinnedMeshShapePart import hkSkinnedMeshShapePart


class hkStorageSkinnedMeshShape(hkSkinnedMeshShape):
    bonesBuffer: any
    boneSets: hkSkinnedMeshShapeBoneSet
    boneSections: hkSkinnedMeshShapeBoneSection
    parts: hkSkinnedMeshShapePart
    name: str

    def __init__(self, infile):
        self.bonesBuffer = any(infile)  # TYPE_ARRAY
        self.boneSets = hkSkinnedMeshShapeBoneSet(infile)  # TYPE_ARRAY
        self.boneSections = hkSkinnedMeshShapeBoneSection(infile)  # TYPE_ARRAY
        self.parts = hkSkinnedMeshShapePart(infile)  # TYPE_ARRAY
        self.name = struct.unpack('>s', infile.read(0))
