from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Player():
  def __init__(self, x, y, w, h, name):
    self.x = x
    self.y = y
    self.width = w
    self.height = h
    self.score = 0
    self.type = name
  
  def _draw_player_(self, window_coordinates, x_step = 0, y_step = 0):
    if self.type=="protagonista":
      glColor3f(0,1,0)
      glBegin(GL_QUADS)
      glVertex2f(self.width*2+self.x*window_coordinates + x_step,self.y+self.height*2+self.y*window_coordinates + y_step)
      glVertex2f(self.width*2+self.x*window_coordinates + x_step,self.y+self.height*3.5+self.y*window_coordinates + y_step)
      glVertex2f(self.width*20+self.x*window_coordinates + x_step,self.y+self.height*3.5+self.y*window_coordinates + y_step)
      glVertex2f(self.width*20+self.x*window_coordinates + x_step,self.y+self.height*2+self.y*window_coordinates + y_step)
      glEnd()

      glColor3f(0,1,0)
      glBegin(GL_QUADS)
      glVertex2f(self.width*3+self.x*window_coordinates + x_step,self.y+self.height*1.5+self.y*window_coordinates + y_step)
      glVertex2f(self.width*3+self.x*window_coordinates + x_step,self.y+self.height*4+self.y*window_coordinates + y_step)
      glVertex2f(self.width*19+self.x*window_coordinates + x_step,self.y+self.height*4+self.y*window_coordinates + y_step)
      glVertex2f(self.width*19+self.x*window_coordinates + x_step,self.y+self.height*1.5+self.y*window_coordinates + y_step)
      glEnd()

      glColor3f(0,1,0)
      glBegin(GL_QUADS)
      glVertex2f(self.width*6+self.x*window_coordinates + x_step,self.y+self.height*1+self.y*window_coordinates + y_step)
      glVertex2f(self.width*6+self.x*window_coordinates + x_step,self.y+self.height*1.5+self.y*window_coordinates + y_step)
      glVertex2f(self.width*16+self.x*window_coordinates + x_step,self.y+self.height*1.5+self.y*window_coordinates + y_step)
      glVertex2f(self.width*16+self.x*window_coordinates + x_step,self.y+self.height*1+self.y*window_coordinates + y_step)
      glEnd()

      glColor3f(0,1,0)
      glBegin(GL_QUADS)
      glVertex2f(self.width*6+self.x*window_coordinates + x_step,self.y+self.height*4+self.y*window_coordinates + y_step)
      glVertex2f(self.width*6+self.x*window_coordinates + x_step,self.y+self.height*6+self.y*window_coordinates + y_step)
      glVertex2f(self.width*10+self.x*window_coordinates + x_step,self.y+self.height*6+self.y*window_coordinates + y_step)
      glVertex2f(self.width*10+self.x*window_coordinates + x_step,self.y+self.height*4+self.y*window_coordinates + y_step)
      glEnd()

      glColor3f(0,1,0)
      glBegin(GL_QUADS)
      glVertex2f(self.width*16+self.x*window_coordinates + x_step,self.y+self.height*4+self.y*window_coordinates + y_step)
      glVertex2f(self.width*16+self.x*window_coordinates + x_step,self.y+self.height*6+self.y*window_coordinates + y_step)
      glVertex2f(self.width*12+self.x*window_coordinates + x_step,self.y+self.height*6+self.y*window_coordinates + y_step)
      glVertex2f(self.width*12+self.x*window_coordinates + x_step,self.y+self.height*4+self.y*window_coordinates + y_step)
      glEnd()

      glColor3f(1,1,1)
      glBegin(GL_QUADS)
      glVertex2f(self.width*7+self.x*window_coordinates + x_step,self.y+self.height*4.5+self.y*window_coordinates + y_step)
      glVertex2f(self.width*7+self.x*window_coordinates + x_step,self.y+self.height*5.5+self.y*window_coordinates + y_step)
      glVertex2f(self.width*9+self.x*window_coordinates + x_step,self.y+self.height*5.5+self.y*window_coordinates + y_step)
      glVertex2f(self.width*9+self.x*window_coordinates + x_step,self.y+self.height*4.5+self.y*window_coordinates + y_step)
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_QUADS)
      glVertex2f(self.width*7.6+self.x*window_coordinates + x_step,self.y+self.height*4.8+self.y*window_coordinates + y_step)
      glVertex2f(self.width*7.6+self.x*window_coordinates + x_step,self.y+self.height*5.2+self.y*window_coordinates + y_step)
      glVertex2f(self.width*8.4+self.x*window_coordinates + x_step,self.y+self.height*5.2+self.y*window_coordinates + y_step)
      glVertex2f(self.width*8.4+self.x*window_coordinates + x_step,self.y+self.height*4.8+self.y*window_coordinates + y_step)
      glEnd()

      glColor(1,1,1)
      glBegin(GL_QUADS)
      glVertex2f(self.width*13+self.x*window_coordinates + x_step,self.y+self.height*4.5+self.y*window_coordinates + y_step)
      glVertex2f(self.width*13+self.x*window_coordinates + x_step,self.y+self.height*5.5+self.y*window_coordinates + y_step)
      glVertex2f(self.width*15+self.x*window_coordinates + x_step,self.y+self.height*5.5+self.y*window_coordinates + y_step)
      glVertex2f(self.width*15+self.x*window_coordinates + x_step,self.y+self.height*4.5+self.y*window_coordinates + y_step)
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_QUADS)
      glVertex2f(self.width*13.6+self.x*window_coordinates + x_step,self.y+self.height*4.8+self.y*window_coordinates + y_step)
      glVertex2f(self.width*13.6+self.x*window_coordinates + x_step,self.y+self.height*5.2+self.y*window_coordinates + y_step)
      glVertex2f(self.width*14.4+self.x*window_coordinates + x_step,self.y+self.height*5.2+self.y*window_coordinates + y_step)
      glVertex2f(self.width*14.4+self.x*window_coordinates + x_step,self.y+self.height*4.8+self.y*window_coordinates + y_step)
      glEnd()

      glColor3f(1,0,0)
      glBegin(GL_LINES)
      glVertex2f(self.width*7+self.x*window_coordinates + x_step,self.y+self.height*2+self.y*window_coordinates + y_step)
      glVertex2f(self.width*15+self.x*window_coordinates + x_step,self.y+self.height*2+self.y*window_coordinates + y_step)
      
      glVertex2f(self.width*7+self.x*window_coordinates + x_step,self.y+self.height*2.3+self.y*window_coordinates + y_step)
      glVertex2f(self.width*7+self.x*window_coordinates + x_step,self.y+self.height*2+self.y*window_coordinates + y_step)

      glVertex2f(self.width*15+self.x*window_coordinates + x_step,self.y+self.height*2.3+self.y*window_coordinates + y_step)
      glVertex2f(self.width*15+self.x*window_coordinates + x_step,self.y+self.height*2+self.y*window_coordinates + y_step)
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_TRIANGLES)
      glVertex2f(self.width*11+self.x*window_coordinates + x_step,self.y+self.height*1+self.y*window_coordinates + y_step)
      glVertex2f(self.width*16+self.x*window_coordinates + x_step,self.y+self.height*2+self.y*window_coordinates + y_step)
      glVertex2f(self.width*16+self.x*window_coordinates + x_step,self.y+self.height*0+self.y*window_coordinates + y_step)
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_TRIANGLES)
      glVertex2f(self.width*11+self.x*window_coordinates + x_step,self.y+self.height*1+self.y*window_coordinates + y_step)
      glVertex2f(self.width*6+self.x*window_coordinates + x_step,self.y+self.height*2+self.y*window_coordinates + y_step)
      glVertex2f(self.width*6+self.x*window_coordinates + x_step,self.y+self.height*0+self.y*window_coordinates + y_step)
      glEnd()

    if self.type=='inimigo':
      glColor3f(1,1,1)
      glBegin(GL_QUADS)
      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width/5))
      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width*0.70))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.80),self.y*window_coordinates + y_step + (self.width*0.70))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.80),self.y*window_coordinates + y_step + (self.width/5))
      glEnd()
      glColor3f(1,1,1)
      glBegin(GL_QUADS)
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.52),self.y*window_coordinates + y_step + (self.width/5))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.52),self.y*window_coordinates + y_step + (self.width*0.75))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.78),self.y*window_coordinates + y_step + (self.width*0.75))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.78),self.y*window_coordinates + y_step + (self.width/5))
      glEnd()

      glColor3f(1,1,1)
      glBegin(GL_QUADS)
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.55),self.y*window_coordinates + y_step + (self.width/5))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.55),self.y*window_coordinates + y_step + (self.width*0.80))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.75),self.y*window_coordinates + y_step + (self.width*0.80))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.75),self.y*window_coordinates + y_step + (self.width/5))
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_QUADS)
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.57),self.y*window_coordinates + y_step + (self.width*0.60))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.57),self.y*window_coordinates + y_step + (self.width*0.65))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.62),self.y*window_coordinates + y_step + (self.width*0.65))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.62),self.y*window_coordinates + y_step + (self.width*0.60))
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_LINES)
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.57),self.y*window_coordinates + y_step + (self.width*0.65))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.63),self.y*window_coordinates + y_step + (self.width*0.68))
      glEnd()

      glColor3f(1,1,0)
      glBegin(GL_TRIANGLES)
      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width*0.55))
      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width*0.70))
      glVertex2f(self.x*window_coordinates + x_step + (self.width/5),self.y*window_coordinates + y_step + (self.width/2))
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_LINES)
      glVertex2f(self.x*window_coordinates + x_step + (self.width/5),self.y*window_coordinates + y_step + (self.width/2))
      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width*0.60))
      glEnd()

      glColor3f(0.8,0.4,0)
      glBegin(GL_POLYGON)
      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width/5))
      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width/2))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.55),self.y*window_coordinates + y_step + (self.width*0.55))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.59),self.y*window_coordinates + y_step + (self.width/2))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.63),self.y*window_coordinates + y_step + (self.width*0.55))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.67),self.y*window_coordinates + y_step + (self.width/2))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.71),self.y*window_coordinates + y_step + (self.width*0.55))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.75),self.y*window_coordinates + y_step + (self.width/2))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.79),self.y*window_coordinates + y_step + (self.width*0.55))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.80),self.y*window_coordinates + y_step + (self.width/2))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.80),self.y*window_coordinates + y_step + (self.width/5))
      glEnd()

      glColor(0,0,0)
      glBegin(GL_LINES)
      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width/5))
      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width*0.55))

      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width*0.55))
      glVertex2f(self.x*window_coordinates + x_step + (self.width/5),self.y*window_coordinates + y_step + (self.width/2))

      glVertex2f(self.x*window_coordinates + x_step + (self.width/5),self.y*window_coordinates + y_step + (self.width/2))
      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width*0.70))

      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width*0.70))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.52),self.y*window_coordinates + y_step + (self.width*0.70))

      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.52),self.y*window_coordinates + y_step + (self.width*0.70))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.52),self.y*window_coordinates + y_step + (self.width*0.75))

      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.52),self.y*window_coordinates + y_step + (self.width*0.75))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.55),self.y*window_coordinates + y_step + (self.width*0.75))

      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.55),self.y*window_coordinates + y_step + (self.width*0.75))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.55),self.y*window_coordinates + y_step + (self.width*0.80))

      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.55),self.y*window_coordinates + y_step + (self.width*0.80))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.75),self.y*window_coordinates + y_step + (self.width*0.80))

      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.75),self.y*window_coordinates + y_step + (self.width*0.80))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.75),self.y*window_coordinates + y_step + (self.width*0.75))

      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.75),self.y*window_coordinates + y_step + (self.width*0.75))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.78),self.y*window_coordinates + y_step + (self.width*0.75))

      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.78),self.y*window_coordinates + y_step + (self.width*0.75))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.78),self.y*window_coordinates + y_step + (self.width*0.70))

      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.78),self.y*window_coordinates + y_step + (self.width*0.70))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.80),self.y*window_coordinates + y_step + (self.width*0.70))

      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.80),self.y*window_coordinates + y_step + (self.width*0.70))
      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.80),self.y*window_coordinates + y_step + (self.width/5))

      glVertex2f(self.x*window_coordinates + x_step + (self.width*0.80),self.y*window_coordinates + y_step + (self.width/5))
      glVertex2f(self.x*window_coordinates + x_step + (self.width/2),self.y*window_coordinates + y_step + (self.width/5))
      glEnd()
