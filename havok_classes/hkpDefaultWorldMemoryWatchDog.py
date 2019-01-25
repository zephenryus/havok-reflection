from .hkWorldMemoryAvailableWatchDog import hkWorldMemoryAvailableWatchDog
import struct


class hkpDefaultWorldMemoryWatchDog(hkWorldMemoryAvailableWatchDog):
    freeHeapMemoryRequested: int

    def __init__(self, infile):
        self.freeHeapMemoryRequested = struct.unpack('>i', infile.read(4))
