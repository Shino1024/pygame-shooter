from enum import Enum

class BehaviourTypes(Enum):
	IDLE,
	WANDERING,
	AGGRESSIVE,
	*_ = range(10)

class Algorithm:
	pass

class IdleBehaviour(Algorithm):
	pass

class WanderingBehaviour(Algorithm):
	pass

class AggressiveBehaviour(Algorithm):
	pass
