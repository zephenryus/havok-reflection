from .hkpConstraintInstance import hkpConstraintInstance
from typing import List
from .common import get_array
from .hkpEntity import hkpEntity
from .hkpConstraintChainInstanceAction import hkpConstraintChainInstanceAction
import struct


class hkpConstraintChainInstance(hkpConstraintInstance):
    chainedEntities: List[hkpEntity]
    action: any
    chainConnectedness: int

    def __init__(self, infile):
        self.chainedEntities = get_array(infile, hkpEntity, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.action = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.chainConnectedness = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID

    def __repr__(self):
        return "<{class_name} chainedEntities=[{chainedEntities}], action={action}, chainConnectedness={chainConnectedness}>".format(**{
            "class_name": self.__class__.__name__,
            "chainedEntities": self.chainedEntities,
            "action": self.action,
            "chainConnectedness": self.chainConnectedness,
        })
