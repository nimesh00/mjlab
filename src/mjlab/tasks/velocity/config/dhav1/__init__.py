import gymnasium as gym

gym.register(
  id="Mjlab-Velocity-Rough-xTerra-Dhav1",
  entry_point="mjlab.envs:ManagerBasedRlEnv",
  disable_env_checker=True,
  kwargs={
    "env_cfg_entry_point": f"{__name__}.rough_env_cfg:xTerraDhav1RoughEnvCfg",
    "rl_cfg_entry_point": f"{__name__}.rl_cfg:xTerraDhav1PPORunnerCfg",
  },
)

gym.register(
  id="Mjlab-Velocity-Rough-xTerra-Dhav1-Play",
  entry_point="mjlab.envs:ManagerBasedRlEnv",
  disable_env_checker=True,
  kwargs={
    "env_cfg_entry_point": f"{__name__}.rough_env_cfg:xTerraDhav1RoughEnvCfg_PLAY",
    "rl_cfg_entry_point": f"{__name__}.rl_cfg:xTerraDhav1PPORunnerCfg",
  },
)

gym.register(
  id="Mjlab-Velocity-Flat-xTerra-Dhav1",
  entry_point="mjlab.envs:ManagerBasedRlEnv",
  disable_env_checker=True,
  kwargs={
    "env_cfg_entry_point": f"{__name__}.flat_env_cfg:xTerraDhav1FlatEnvCfg",
    "rl_cfg_entry_point": f"{__name__}.rl_cfg:xTerraDhav1PPORunnerCfg",
  },
)

gym.register(
  id="Mjlab-Velocity-Flat-xTerra-Dhav1-Play",
  entry_point="mjlab.envs:ManagerBasedRlEnv",
  disable_env_checker=True,
  kwargs={
    "env_cfg_entry_point": f"{__name__}.flat_env_cfg:xTerraDhav1FlatEnvCfg_PLAY",
    "rl_cfg_entry_point": f"{__name__}.rl_cfg:xTerraDhav1PPORunnerCfg",
  },
)
