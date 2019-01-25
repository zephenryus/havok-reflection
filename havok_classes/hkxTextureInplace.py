from .hkReferencedObject import hkReferencedObject
import struct
from typing import List
from .common import get_array


class hkxTextureInplace(hkReferencedObject):
    fileType: str
    data: List[int]
    name: str
    originalFilename: str

    def __init__(self, infile):
        self.fileType = struct.unpack('>c', infile.read(1))  # TYPE_CHAR:TYPE_VOID
        self.data = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.originalFilename = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} fileType=\"{fileType}\", data=[{data}], name=\"{name}\", originalFilename=\"{originalFilename}\">".format(**{
            "class_name": self.__class__.__name__,
            "fileType": self.fileType,
            "data": self.data,
            "name": self.name,
            "originalFilename": self.originalFilename,
        })
