from .hkBitFieldStoragehkArrayunsignedinthkContainerHeapAllocator import hkBitFieldStoragehkArrayunsignedinthkContainerHeapAllocator


class hkBitFieldBasehkBitFieldStoragehkArrayunsignedinthkContainerHeapAllocator(object):
    storage: hkBitFieldStoragehkArrayunsignedinthkContainerHeapAllocator

    def __init__(self, infile):
        self.storage = hkBitFieldStoragehkArrayunsignedinthkContainerHeapAllocator(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} storage={storage}>".format(**{
            "class_name": self.__class__.__name__,
            "storage": self.storage,
        })
