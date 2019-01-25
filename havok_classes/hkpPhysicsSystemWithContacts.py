from .hkpPhysicsSystem import hkpPhysicsSystem
from .hkpSerializedAgentNnEntry import hkpSerializedAgentNnEntry


class hkpPhysicsSystemWithContacts(hkpPhysicsSystem):
    contacts: hkpSerializedAgentNnEntry

    def __init__(self, infile):
        self.contacts = hkpSerializedAgentNnEntry(infile)  # TYPE_ARRAY
