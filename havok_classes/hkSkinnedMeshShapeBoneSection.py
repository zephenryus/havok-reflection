from .hkMeshShape import hkMeshShape
import struct


class hkSkinnedMeshShapeBoneSection(object):
    meshBuffer: hkMeshShape
    startBoneSetId: int
    numBoneSets: int

    def __init__(self, infile):
        self.meshBuffer = hkMeshShape(infile)  # TYPE_POINTER
        self.startBoneSetId = struct.unpack('>H', infile.read(2))
        self.numBoneSets = struct.unpack('>h', infile.read(2))
