import random
import numpy as np

class Ball():
  def __init__(self, x, y, w, h, s):
    self.x = x
    self.y = y
    self.width = w
    self.height = h
    self.ball_speed = s
    self.xstep = self.ball_speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -self.ball_speed*np.cos(np.pi/4)
    _y_direction = random.choice([np.pi/(i/10) for i in range(25,150)])
    self.ystep = self.ball_speed*(np.sin(_y_direction)) if random.randint(0,1) == 1 else -self.ball_speed*(np.sin(_y_direction))
