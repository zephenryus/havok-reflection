from .hkaiAstarCostModifier import hkaiAstarCostModifier


class hkaiDefaultAstarCostModifier(hkaiAstarCostModifier):
	maxCostPenalty: float
	costMultiplierLookupTable: int
