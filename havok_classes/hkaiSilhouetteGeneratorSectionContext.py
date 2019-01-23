from .hkQTransform import hkQTransform
from .hkaiSilhouetteGenerator import hkaiSilhouetteGenerator


class hkaiSilhouetteGeneratorSectionContext(object):
	lastRelativeTransform: hkQTransform
	generator: hkaiSilhouetteGenerator
	generatorSize: int
	generatedLastFrame: bool
	generatingThisFrame: bool
