from typing import Any

from ..envs.poly_commute_like_terms import PolyCommuteLikeTerms
from ..types import MathyEnvDifficulty, MathyEnvProblemArgs
from .gym_goal_env import MathyGymGoalEnv
from .mathy_gym_env import MathyGymEnv, safe_register

#
# Combine like terms without commuting
#


class GymPolynomialCommuteLikeTerms(MathyGymEnv):
    def __init__(self, difficulty: MathyEnvDifficulty, **kwargs: Any):
        super(GymPolynomialCommuteLikeTerms, self).__init__(
            env_class=PolyCommuteLikeTerms,
            env_problem_args=MathyEnvProblemArgs(difficulty=difficulty),
            **kwargs
        )


class PolynomialCommuteLikeTermsEasy(GymPolynomialCommuteLikeTerms):
    def __init__(self, **kwargs: Any):
        super(PolynomialCommuteLikeTermsEasy, self).__init__(
            difficulty=MathyEnvDifficulty.easy, **kwargs
        )


class PolynomialCommuteLikeTermsNormal(GymPolynomialCommuteLikeTerms):
    def __init__(self, **kwargs: Any):
        super(PolynomialCommuteLikeTermsNormal, self).__init__(
            difficulty=MathyEnvDifficulty.normal, **kwargs
        )


class PolynomialCommuteLikeTermsHard(GymPolynomialCommuteLikeTerms):
    def __init__(self, **kwargs: Any):
        super(PolynomialCommuteLikeTermsHard, self).__init__(
            difficulty=MathyEnvDifficulty.hard, **kwargs
        )


safe_register(
    id="mathy-poly-commute-easy-v0",
    entry_point="mathy_envs.gym:PolynomialCommuteLikeTermsEasy",
)
safe_register(
    id="mathy-poly-commute-normal-v0",
    entry_point="mathy_envs.gym:PolynomialCommuteLikeTermsNormal",
)
safe_register(
    id="mathy-poly-commute-hard-v0",
    entry_point="mathy_envs.gym:PolynomialCommuteLikeTermsHard",
)


class GymGoalPolynomialCommuteLikeTerms(MathyGymGoalEnv):
    def __init__(self, difficulty: MathyEnvDifficulty, **kwargs: Any):
        super(GymGoalPolynomialCommuteLikeTerms, self).__init__(
            env_class=PolyCommuteLikeTerms,
            env_problem_args=MathyEnvProblemArgs(difficulty=difficulty),
            **kwargs
        )


class PolynomialCommuteLikeTermsGoalEasy(GymGoalPolynomialCommuteLikeTerms):
    def __init__(self, **kwargs: Any):
        super(PolynomialCommuteLikeTermsGoalEasy, self).__init__(
            difficulty=MathyEnvDifficulty.easy, **kwargs
        )


class PolynomialCommuteLikeTermsGoalNormal(GymGoalPolynomialCommuteLikeTerms):
    def __init__(self, **kwargs: Any):
        super(PolynomialCommuteLikeTermsGoalNormal, self).__init__(
            difficulty=MathyEnvDifficulty.normal, **kwargs
        )


class PolynomialCommuteLikeTermsGoalHard(GymGoalPolynomialCommuteLikeTerms):
    def __init__(self, **kwargs: Any):
        super(PolynomialCommuteLikeTermsGoalHard, self).__init__(
            difficulty=MathyEnvDifficulty.hard, **kwargs
        )


# Goal envs
safe_register(
    id="mathy-goal-poly-commute-easy-v0",
    entry_point="mathy_envs.gym:PolynomialCommuteLikeTermsGoalEasy",
)
safe_register(
    id="mathy-goal-poly-commute-normal-v0",
    entry_point="mathy_envs.gym:PolynomialCommuteLikeTermsGoalNormal",
)
safe_register(
    id="mathy-goal-poly-commute-hard-v0",
    entry_point="mathy_envs.gym:PolynomialCommuteLikeTermsGoalHard",
)
