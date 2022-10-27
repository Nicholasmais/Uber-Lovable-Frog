import random
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Ball():
  def __init__(self, x, y, r, s):
    self.x = x
    self.y = y
    self.radius = r    
    self.points = 50
    self.ball_speed = s
    self.xstep = self.ball_speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -self.ball_speed*np.cos(np.pi/4)
    _y_direction = random.choice([np.pi/(i/10) for i in range(25,150)])
    self.ystep = self.ball_speed*(np.sin(_y_direction)) if random.randint(0,1) == 1 else -self.ball_speed*(np.sin(_y_direction))

  def _draw_ball_(self, window_coordinates, red=0):
    if red:
      glBegin(GL_POLYGON)
      glColor3f(0,0,1)
      for i in range(self.points):
          cos = self.radius * np.cos(i * 2 * np.pi / self.points) + self.x*window_coordinates + self.xstep
          sin = 1.5*self.radius * np.sin(i * 2 * np.pi / self.points) + self.y*window_coordinates + self.ystep
          glVertex2f(cos, sin)
      glEnd()

      glColor(1,0,0)
      glBegin(GL_POLYGON)
      glVertex2f(1.8*self.radius - 2*self.radius + self.x*window_coordinates + self.xstep,3.5*self.radius- 2*self.radius+self.y*window_coordinates + self.ystep)
      glVertex2f(2.2*self.radius- 2*self.radius+ self.x*window_coordinates + self.xstep,3.5*self.radius- 2*self.radius+self.y*window_coordinates + self.ystep)
      glVertex2f(2.2*self.radius- 2*self.radius+ self.x*window_coordinates + self.xstep,.5*self.radius- 2*self.radius+self.y*window_coordinates + self.ystep)
      glVertex2f(1.8*self.radius- 2*self.radius+ self.x*window_coordinates + self.xstep,.5*self.radius- 2*self.radius+self.y*window_coordinates + self.ystep)
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(self.radius- 2*self.radius+ self.x*window_coordinates + self.xstep,1.8*self.radius- 2*self.radius+self.y*window_coordinates + self.ystep)
      glVertex2f(self.radius- 2*self.radius+ self.x*window_coordinates + self.xstep,2.2*self.radius- 2*self.radius+self.y*window_coordinates + self.ystep)
      glVertex2f(3*self.radius- 2*self.radius+ self.x*window_coordinates + self.xstep,2.2*self.radius- 2*self.radius+self.y*window_coordinates + self.ystep)
      glVertex2f(3*self.radius- 2*self.radius+ self.x*window_coordinates + self.xstep,1.8*self.radius- 2*self.radius+self.y*window_coordinates + self.ystep)
      glEnd()
    
    else:
      glColor3f(.5, .5, .5)

      glBegin(GL_POLYGON)
      glColor3f(1,1,1)
      for i in range(self.points):
          cos = self.radius * np.cos(i * 2 * np.pi / self.points) + self.x*window_coordinates + self.xstep
          sin = 1.5*self.radius * np.sin(i * 2 * np.pi / self.points) + self.y*window_coordinates + self.ystep
          glVertex2f(cos, sin)
      glEnd()
