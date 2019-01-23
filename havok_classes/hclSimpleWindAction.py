from .hclAction import hclAction


class hclSimpleWindAction(hclAction):
	windDirection: any
	windMinSpeed: float
	windMaxSpeed: float
	windFrequency: float
	maximumDrag: float
	airVelocity: any
	currentTime: float
