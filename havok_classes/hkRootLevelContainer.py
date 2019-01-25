from .hkRootLevelContainerNamedVariant import hkRootLevelContainerNamedVariant


class hkRootLevelContainer(object):
    namedVariants: hkRootLevelContainerNamedVariant

    def __init__(self, infile):
        self.namedVariants = hkRootLevelContainerNamedVariant(infile)  # TYPE_ARRAY
