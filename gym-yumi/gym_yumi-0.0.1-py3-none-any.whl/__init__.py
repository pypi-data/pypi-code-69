from gym.envs.registration import register

register(
    id='yumi-v0',
    entry_point='gym_yumi.envs:YumiEnv',
)


