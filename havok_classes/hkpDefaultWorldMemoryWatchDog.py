from .hkWorldMemoryAvailableWatchDog import hkWorldMemoryAvailableWatchDog
import struct


class hkpDefaultWorldMemoryWatchDog(hkWorldMemoryAvailableWatchDog):
    freeHeapMemoryRequested: int

    def __init__(self, infile):
        self.freeHeapMemoryRequested = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} freeHeapMemoryRequested={freeHeapMemoryRequested}>".format(**{
            "class_name": self.__class__.__name__,
            "freeHeapMemoryRequested": self.freeHeapMemoryRequested,
        })
