from .hkpPhysicsSystem import hkpPhysicsSystem
from typing import List
from .common import get_array
from .hkpSerializedAgentNnEntry import hkpSerializedAgentNnEntry


class hkpPhysicsSystemWithContacts(hkpPhysicsSystem):
    contacts: List[hkpSerializedAgentNnEntry]

    def __init__(self, infile):
        self.contacts = get_array(infile, hkpSerializedAgentNnEntry, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} contacts=[{contacts}]>".format(**{
            "class_name": self.__class__.__name__,
            "contacts": self.contacts,
        })
