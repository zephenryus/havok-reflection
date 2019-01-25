from .hkReferencedObject import hkReferencedObject
from .hkaiPathfindingUtilFindPathInput import hkaiPathfindingUtilFindPathInput
from .hkaiPathfindingUtilFindPathOutput import hkaiPathfindingUtilFindPathOutput
import struct


class hkaiNavMeshPathRequestInfo(hkReferencedObject):
    input: any
    output: any
    priority: int
    owner: any
    markedForDeletion: bool

    def __init__(self, infile):
        self.input = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.output = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.priority = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.owner = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.markedForDeletion = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} input={input}, output={output}, priority={priority}, owner={owner}, markedForDeletion={markedForDeletion}>".format(**{
            "class_name": self.__class__.__name__,
            "input": self.input,
            "output": self.output,
            "priority": self.priority,
            "owner": self.owner,
            "markedForDeletion": self.markedForDeletion,
        })
