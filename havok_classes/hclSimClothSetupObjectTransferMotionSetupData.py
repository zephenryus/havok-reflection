from .hclTransformSetSetupObject import hclTransformSetSetupObject


class hclSimClothSetupObjectTransferMotionSetupData(object):
	transferMotionTransformSetSetup: hclTransformSetSetupObject
	transferMotionTransformName: any
	transferTranslationMotion: bool
	minTranslationSpeed: float
	maxTranslationSpeed: float
	minTranslationBlend: float
	maxTranslationBlend: float
	transferRotationMotion: bool
	minRotationSpeed: float
	maxRotationSpeed: float
	minRotationBlend: float
	maxRotationBlend: float
