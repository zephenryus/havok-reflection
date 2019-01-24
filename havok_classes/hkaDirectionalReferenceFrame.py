from .hkaParameterizedReferenceFrame import hkaParameterizedReferenceFrame
from .common import vector4


class hkaDirectionalReferenceFrame(hkaParameterizedReferenceFrame):
    movementDir: vector4
