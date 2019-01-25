from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import KeyboardKey
from typing import List
from .common import get_array


class Type(Enum):
    WEAPON_TYPE_INVALID = 0
    WEAPON_TYPE_BALLGUN = 1
    WEAPON_TYPE_GRENADEGUN = 2
    WEAPON_TYPE_GRAVITYGUN = 3
    WEAPON_TYPE_MOUNTEDBALLGUN = 4
    WEAPON_TYPE_TWEAKERGUN = 5
    WEAPON_TYPE_MISSILEGUN = 6
    WEAPON_TYPE_RAYCASTGUN = 7
    WEAPON_TYPE_SPHEREGUN = 8
    WEAPON_TYPE_STICKYGUN = 9
    WEAPON_TYPE_NUM_TYPES = 10


class KeyboardKey(Enum):
    KEY_F1 = 112
    KEY_F2 = 113
    KEY_F3 = 114
    KEY_F4 = 115
    KEY_F5 = 116
    KEY_F6 = 117
    KEY_F7 = 118
    KEY_F8 = 119
    KEY_F9 = 120
    KEY_F10 = 121
    KEY_F11 = 122
    KEY_F12 = 123


class hkpFirstPersonGun(hkReferencedObject):
    type: enumerate
    name: str
    keyboardKey: KeyboardKey
    listeners: List[any]

    def __init__(self, infile):
        self.type = enumerate(infile)  # TYPE_ENUM:TYPE_UINT8
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.keyboardKey = KeyboardKey(infile)  # TYPE_ENUM:TYPE_UINT8
        self.listeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} type={type}, name=\"{name}\", keyboardKey={keyboardKey}, listeners=[{listeners}]>".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
            "name": self.name,
            "keyboardKey": self.keyboardKey,
            "listeners": self.listeners,
        })
