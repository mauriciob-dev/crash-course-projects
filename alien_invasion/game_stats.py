from scoreboard import Scoreboard

class GameStats:

  def __init__(self, ai_game):
    self.high_score = 0
    self.score = None
    self.ships_left = None
    self.settings = ai_game.settings
    self.reset_stats()
    self.game_active = False
    self.high_score_path_file = "files/highscores.txt"
    self.read_high_score()

  def reset_stats(self):
    self.ships_left = self.settings.ship_limit
    self.score = 0

  def read_high_score(self):
    with open(self.high_score_path_file) as file_object:
      contents = file_object.read()
      high_score = int(contents) if contents.strip() else 0
    self.high_score = high_score

  def save_high_score(self):
    with open(self.high_score_path_file, 'w') as file_object:
      file_object.write(str(self.score))
