from .hkWorldMemoryAvailableWatchDog import hkWorldMemoryAvailableWatchDog


class hkpDefaultWorldMemoryWatchDog(hkWorldMemoryAvailableWatchDog):
    freeHeapMemoryRequested: int
