from .hkReferencedObject import hkReferencedObject
import struct
from .common import any


class hkxTextureInplace(hkReferencedObject):
    fileType: str
    data: any
    name: str
    originalFilename: str

    def __init__(self, infile):
        self.fileType = struct.unpack('>c', infile.read(1))
        self.data = any(infile)  # TYPE_ARRAY
        self.name = struct.unpack('>s', infile.read(0))
        self.originalFilename = struct.unpack('>s', infile.read(0))
