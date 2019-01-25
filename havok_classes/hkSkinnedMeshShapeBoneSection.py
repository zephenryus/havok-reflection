from .hkMeshShape import hkMeshShape
import struct


class hkSkinnedMeshShapeBoneSection(object):
    meshBuffer: any
    startBoneSetId: int
    numBoneSets: int

    def __init__(self, infile):
        self.meshBuffer = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.startBoneSetId = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.numBoneSets = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} meshBuffer={meshBuffer}, startBoneSetId={startBoneSetId}, numBoneSets={numBoneSets}>".format(**{
            "class_name": self.__class__.__name__,
            "meshBuffer": self.meshBuffer,
            "startBoneSetId": self.startBoneSetId,
            "numBoneSets": self.numBoneSets,
        })
