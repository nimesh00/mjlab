from dataclasses import dataclass

from mjlab.tasks.velocity.config.dhav1.rough_env_cfg import (
  xTerraDhav1RoughEnvCfg,
)


@dataclass
class xTerraDhav1FlatEnvCfg(xTerraDhav1RoughEnvCfg):
  def __post_init__(self):
    super().__post_init__()

    assert self.scene.terrain is not None
    self.scene.terrain.terrain_type = "plane"
    self.scene.terrain.terrain_generator = None
    self.curriculum.terrain_levels = None


@dataclass
class xTerraDhav1FlatEnvCfg_PLAY(xTerraDhav1FlatEnvCfg):
  def __post_init__(self):
    super().__post_init__()

    # Effectively infinite episode length.
    self.episode_length_s = int(1e9)

    self.observations.policy.enable_corruption = False
    self.events.push_robot = None
