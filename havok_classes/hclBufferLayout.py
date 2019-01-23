from .hclBufferLayoutBufferElement import hclBufferLayoutBufferElement
from .hclBufferLayoutSlot import hclBufferLayoutSlot


class hclBufferLayout(object):
	elementsLayout: hclBufferLayoutBufferElement
	slots: hclBufferLayoutSlot
	numSlots: int
	triangleFormat: any
