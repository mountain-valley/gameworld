import gymnasium as gym


class GameworldEnv(gym.Env):

    def __init__(self, **kwargs):
        super().__init__()

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        # override with reset logic in subclasses

    def step(self, action):
        # override with step logic
        reward = 0
        done = False
        return (
            self._get_obs(),
            reward,
            done,
            False,
            {},
        )

    def _get_obs(self):
        # override with observation logic
        pass
