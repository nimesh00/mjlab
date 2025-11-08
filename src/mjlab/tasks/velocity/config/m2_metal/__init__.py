import gymnasium as gym

gym.register(
  id="Mjlab-Velocity-Rough-xTerra-M2Metal",
  entry_point="mjlab.envs:ManagerBasedRlEnv",
  disable_env_checker=True,
  kwargs={
    "env_cfg_entry_point": f"{__name__}.rough_env_cfg:xTerraM2MetalRoughEnvCfg",
    "rl_cfg_entry_point": f"{__name__}.rl_cfg:xTerraM2MetalPPORunnerCfg",
  },
)

gym.register(
  id="Mjlab-Velocity-Rough-xTerra-M2Metal-Play",
  entry_point="mjlab.envs:ManagerBasedRlEnv",
  disable_env_checker=True,
  kwargs={
    "env_cfg_entry_point": f"{__name__}.rough_env_cfg:xTerraM2MetalRoughEnvCfg_PLAY",
    "rl_cfg_entry_point": f"{__name__}.rl_cfg:xTerraM2MetalPPORunnerCfg",
  },
)

gym.register(
  id="Mjlab-Velocity-Flat-xTerra-M2Metal",
  entry_point="mjlab.envs:ManagerBasedRlEnv",
  disable_env_checker=True,
  kwargs={
    "env_cfg_entry_point": f"{__name__}.flat_env_cfg:xTerraM2MetalFlatEnvCfg",
    "rl_cfg_entry_point": f"{__name__}.rl_cfg:xTerraM2MetalPPORunnerCfg",
  },
)

gym.register(
  id="Mjlab-Velocity-Flat-xTerra-M2Metal-Play",
  entry_point="mjlab.envs:ManagerBasedRlEnv",
  disable_env_checker=True,
  kwargs={
    "env_cfg_entry_point": f"{__name__}.flat_env_cfg:xTerraM2MetalFlatEnvCfg_PLAY",
    "rl_cfg_entry_point": f"{__name__}.rl_cfg:xTerraM2MetalPPORunnerCfg",
  },
)
