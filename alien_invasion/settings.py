class Settings:

  def __init__(self):
    self.alien_points = None
    self.fleet_direction = None
    self.alien_speed = None
    self.bullet_speed = None
    self.ship_speed = None
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230, 230, 230)

    self.ship_limit = 3

    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60, 60, 60)
    self.bullet_allowed = 3

    self.fleet_drop_speed = 10

    self.speedup_scale = 1.1
    self.score_scale = 1.5

    self.initialize_dynamic_settings()

  def initialize_dynamic_settings(self):
    self.ship_speed =  0.5
    self.bullet_speed = 1.5
    self.alien_speed =  1.0
    # fleet_direction of 1 represents right; -1 represents left.
    self.fleet_direction = 1

    self.alien_points = 50

  def increase_speed(self):
    self.ship_speed *= self.speedup_scale
    self.bullet_speed *= self.speedup_scale
    self.alien_speed *= self.speedup_scale
    self.alien_points = int(self.alien_points * self.score_scale)
