from .hkpPhysicsSystem import hkpPhysicsSystem
from .hkpSerializedAgentNnEntry import hkpSerializedAgentNnEntry


class hkpPhysicsSystemWithContacts(hkpPhysicsSystem):
    contacts: hkpSerializedAgentNnEntry
