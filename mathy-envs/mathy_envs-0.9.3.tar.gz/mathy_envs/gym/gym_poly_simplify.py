from typing import Any

from ..envs.poly_simplify import PolySimplify
from ..types import MathyEnvDifficulty, MathyEnvProblemArgs
from .gym_goal_env import MathyGymGoalEnv
from .mathy_gym_env import MathyGymEnv, safe_register


class GymPolynomialSimplification(MathyGymEnv):
    def __init__(self, difficulty: MathyEnvDifficulty, **kwargs: Any):
        super(GymPolynomialSimplification, self).__init__(
            env_class=PolySimplify,
            env_problem_args=MathyEnvProblemArgs(difficulty=difficulty),
            **kwargs
        )


class PolynomialsEasy(GymPolynomialSimplification):
    def __init__(self, **kwargs: Any):
        super(PolynomialsEasy, self).__init__(
            difficulty=MathyEnvDifficulty.easy, **kwargs
        )


class PolynomialsNormal(GymPolynomialSimplification):
    def __init__(self, **kwargs: Any):
        super(PolynomialsNormal, self).__init__(
            difficulty=MathyEnvDifficulty.normal, **kwargs
        )


class PolynomialsHard(GymPolynomialSimplification):
    def __init__(self, **kwargs: Any):
        super(PolynomialsHard, self).__init__(
            difficulty=MathyEnvDifficulty.hard, **kwargs
        )


safe_register(id="mathy-poly-easy-v0", entry_point="mathy_envs.gym:PolynomialsEasy")
safe_register(id="mathy-poly-normal-v0", entry_point="mathy_envs.gym:PolynomialsNormal")
safe_register(id="mathy-poly-hard-v0", entry_point="mathy_envs.gym:PolynomialsHard")


class GymGoalPolynomialSimplification(MathyGymGoalEnv):
    def __init__(self, difficulty: MathyEnvDifficulty, **kwargs: Any):
        super(GymGoalPolynomialSimplification, self).__init__(
            env_class=PolySimplify,
            env_problem_args=MathyEnvProblemArgs(difficulty=difficulty),
            **kwargs
        )


class PolynomialsGoalEasy(GymGoalPolynomialSimplification):
    def __init__(self, **kwargs: Any):
        super(PolynomialsGoalEasy, self).__init__(
            difficulty=MathyEnvDifficulty.easy, **kwargs
        )


class PolynomialsGoalNormal(GymGoalPolynomialSimplification):
    def __init__(self, **kwargs: Any):
        super(PolynomialsGoalNormal, self).__init__(
            difficulty=MathyEnvDifficulty.normal, **kwargs
        )


class PolynomialsGoalHard(GymGoalPolynomialSimplification):
    def __init__(self, **kwargs: Any):
        super(PolynomialsGoalHard, self).__init__(
            difficulty=MathyEnvDifficulty.hard, **kwargs
        )


# Goal envs
safe_register(
    id="mathy-goal-poly-easy-v0", entry_point="mathy_envs.gym:PolynomialsGoalEasy"
)
safe_register(
    id="mathy-goal-poly-normal-v0",
    entry_point="mathy_envs.gym:PolynomialsGoalNormal",
)
safe_register(
    id="mathy-goal-poly-hard-v0", entry_point="mathy_envs.gym:PolynomialsGoalHard"
)
