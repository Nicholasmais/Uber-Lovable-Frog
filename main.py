#https://www.youtube.com/watch?v=a4NVQC_2S2U&t=64s&ab_channel=NaseemShah
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random
import numpy as np
from classes.player import Player
from classes.ball import Ball

import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pause_game = True
end_game = False
game_time_limit = 35
remaining_time = game_time_limit
hold_time = 0
reset_time = 0
timer_red = 0
delta_time_red = 0

window_coordinates = 100
player_width = 5
player_height = 10

player1 = Player(-1,0,player_width/10,player_height/4)
player2 = Player(.775,0,player_width*5,player_height/4)

points = 50

ball = Ball(0,0,5,0.035)
red_ball = Ball(0,0,5,0.025)

radius = 25
radius2 = 23
radius3 = 2

def Background(x1 = -100, y1=0):
    glColor3f(1,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2f(x1+(0),y1+(0))
    glVertex2f(x1+(0),y1+(600))
    glVertex2f(x1+(3),y1+(600))
    glVertex2f(x1+(3),y1+(0))
    glEnd()
    
    glColor3f(1,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2f(x1+(497),y1+(0))
    glVertex2f(x1+(497),y1+(600))
    glVertex2f(x1+(500),y1+(600))
    glVertex2f(x1+(500),y1+(0))
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(x1+(0),y1+(0))
    glVertex2f(x1+(500),y1+(0))
    glVertex2f(x1+(500),y1+(5))
    glVertex2f(x1+(0),y1+(5))
    glEnd()

    glColor(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(x1+(0),y1+(245))
    glVertex2f(x1+(500),y1+(245))
    glVertex2f(x1+(500),y1+(600))
    glVertex2f(x1+(0),y1+(600))
    glEnd()

    glColor(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(x1+(248),y1+(5))
    glVertex2f(x1+(251),y1+(5))
    glVertex2f(x1+(251),y1+(245))
    glVertex2f(x1+(248),y1+(245))
    glEnd()

    

    import math
    

    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    for i in range(points):
        cos = radius * math.cos(i * 2 * math.pi / points) + x1+(250)
        sin = radius * math.sin(i * 2 * math.pi / points) + y1+(125)
        glVertex2f(cos, sin)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.3,0.8,1)
    for i in range(points):
        cos = radius2 * math.cos(i * 2 * math.pi / points) + x1+(250)
        sin = radius2 * math.sin(i * 2 * math.pi / points) + y1+(125)
        glVertex2f(cos, sin)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    for i in range(points):
        cos = radius3 * math.cos(i * 2 * math.pi / points) + x1+(250)
        sin = radius3 * math.sin(i * 2 * math.pi / points) + y1+(125)
        glVertex2f(cos, sin)
    glEnd()

def DesenhaObjeto(width, height, x, y, x_step = 0, y_step = 0):
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t

  glColor3f(.5, .5, .5)
  glBegin(GL_QUADS)

  glVertex2f(-1*width + x*window_coordinates + x_step,-1*height + y*window_coordinates + y_step)
  glVertex2f(-1*width + x*window_coordinates + x_step,1*height + y*window_coordinates + y_step)
  glVertex2f(1*width + x*window_coordinates + x_step,1*height + y*window_coordinates + y_step)
  glVertex2f(1*width + x*window_coordinates + x_step,-1*height + y*window_coordinates + y_step)

  glEnd()

def DesenhaPlayer1(x, y, x_step = 0, y_step = 0):
  glColor3f(0,1,0)
  glBegin(GL_QUADS)
  glVertex2f(player1.width*2+x*window_coordinates + x_step,y+player1.height*2+y*window_coordinates + y_step)
  glVertex2f(player1.width*2+x*window_coordinates + x_step,y+player1.height*3.5+y*window_coordinates + y_step)
  glVertex2f(player1.width*20+x*window_coordinates + x_step,y+player1.height*3.5+y*window_coordinates + y_step)
  glVertex2f(player1.width*20+x*window_coordinates + x_step,y+player1.height*2+y*window_coordinates + y_step)
  glEnd()

  glColor3f(0,1,0)
  glBegin(GL_QUADS)
  glVertex2f(player1.width*3+x*window_coordinates + x_step,y+player1.height*1.5+y*window_coordinates + y_step)
  glVertex2f(player1.width*3+x*window_coordinates + x_step,y+player1.height*4+y*window_coordinates + y_step)
  glVertex2f(player1.width*19+x*window_coordinates + x_step,y+player1.height*4+y*window_coordinates + y_step)
  glVertex2f(player1.width*19+x*window_coordinates + x_step,y+player1.height*1.5+y*window_coordinates + y_step)
  glEnd()

  glColor3f(0,1,0)
  glBegin(GL_QUADS)
  glVertex2f(player1.width*6+x*window_coordinates + x_step,y+player1.height*1+y*window_coordinates + y_step)
  glVertex2f(player1.width*6+x*window_coordinates + x_step,y+player1.height*1.5+y*window_coordinates + y_step)
  glVertex2f(player1.width*16+x*window_coordinates + x_step,y+player1.height*1.5+y*window_coordinates + y_step)
  glVertex2f(player1.width*16+x*window_coordinates + x_step,y+player1.height*1+y*window_coordinates + y_step)
  glEnd()

  glColor3f(0,1,0)
  glBegin(GL_QUADS)
  glVertex2f(player1.width*6+x*window_coordinates + x_step,y+player1.height*4+y*window_coordinates + y_step)
  glVertex2f(player1.width*6+x*window_coordinates + x_step,y+player1.height*6+y*window_coordinates + y_step)
  glVertex2f(player1.width*10+x*window_coordinates + x_step,y+player1.height*6+y*window_coordinates + y_step)
  glVertex2f(player1.width*10+x*window_coordinates + x_step,y+player1.height*4+y*window_coordinates + y_step)
  glEnd()

  glColor3f(0,1,0)
  glBegin(GL_QUADS)
  glVertex2f(player1.width*16+x*window_coordinates + x_step,y+player1.height*4+y*window_coordinates + y_step)
  glVertex2f(player1.width*16+x*window_coordinates + x_step,y+player1.height*6+y*window_coordinates + y_step)
  glVertex2f(player1.width*12+x*window_coordinates + x_step,y+player1.height*6+y*window_coordinates + y_step)
  glVertex2f(player1.width*12+x*window_coordinates + x_step,y+player1.height*4+y*window_coordinates + y_step)
  glEnd()

  glColor3f(1,1,1)
  glBegin(GL_QUADS)
  glVertex2f(player1.width*7+x*window_coordinates + x_step,y+player1.height*4.5+y*window_coordinates + y_step)
  glVertex2f(player1.width*7+x*window_coordinates + x_step,y+player1.height*5.5+y*window_coordinates + y_step)
  glVertex2f(player1.width*9+x*window_coordinates + x_step,y+player1.height*5.5+y*window_coordinates + y_step)
  glVertex2f(player1.width*9+x*window_coordinates + x_step,y+player1.height*4.5+y*window_coordinates + y_step)
  glEnd()

  glColor3f(0,0,0)
  glBegin(GL_QUADS)
  glVertex2f(player1.width*7.6+x*window_coordinates + x_step,y+player1.height*4.8+y*window_coordinates + y_step)
  glVertex2f(player1.width*7.6+x*window_coordinates + x_step,y+player1.height*5.2+y*window_coordinates + y_step)
  glVertex2f(player1.width*8.4+x*window_coordinates + x_step,y+player1.height*5.2+y*window_coordinates + y_step)
  glVertex2f(player1.width*8.4+x*window_coordinates + x_step,y+player1.height*4.8+y*window_coordinates + y_step)
  glEnd()

  glColor(1,1,1)
  glBegin(GL_QUADS)
  glVertex2f(player1.width*13+x*window_coordinates + x_step,y+player1.height*4.5+y*window_coordinates + y_step)
  glVertex2f(player1.width*13+x*window_coordinates + x_step,y+player1.height*5.5+y*window_coordinates + y_step)
  glVertex2f(player1.width*15+x*window_coordinates + x_step,y+player1.height*5.5+y*window_coordinates + y_step)
  glVertex2f(player1.width*15+x*window_coordinates + x_step,y+player1.height*4.5+y*window_coordinates + y_step)
  glEnd()

  glColor3f(0,0,0)
  glBegin(GL_QUADS)
  glVertex2f(player1.width*13.6+x*window_coordinates + x_step,y+player1.height*4.8+y*window_coordinates + y_step)
  glVertex2f(player1.width*13.6+x*window_coordinates + x_step,y+player1.height*5.2+y*window_coordinates + y_step)
  glVertex2f(player1.width*14.4+x*window_coordinates + x_step,y+player1.height*5.2+y*window_coordinates + y_step)
  glVertex2f(player1.width*14.4+x*window_coordinates + x_step,y+player1.height*4.8+y*window_coordinates + y_step)
  glEnd()

  glColor3f(1,0,0)
  glBegin(GL_LINES)
  glVertex2f(player1.width*7+x*window_coordinates + x_step,y+player1.height*2+y*window_coordinates + y_step)
  glVertex2f(player1.width*15+x*window_coordinates + x_step,y+player1.height*2+y*window_coordinates + y_step)
  
  glVertex2f(player1.width*7+x*window_coordinates + x_step,y+player1.height*2.3+y*window_coordinates + y_step)
  glVertex2f(player1.width*7+x*window_coordinates + x_step,y+player1.height*2+y*window_coordinates + y_step)

  glVertex2f(player1.width*15+x*window_coordinates + x_step,y+player1.height*2.3+y*window_coordinates + y_step)
  glVertex2f(player1.width*15+x*window_coordinates + x_step,y+player1.height*2+y*window_coordinates + y_step)
  glEnd()

  glColor3f(0,0,0)
  glBegin(GL_TRIANGLES)
  glVertex2f(player1.width*11+x*window_coordinates + x_step,y+player1.height*1+y*window_coordinates + y_step)
  glVertex2f(player1.width*16+x*window_coordinates + x_step,y+player1.height*2+y*window_coordinates + y_step)
  glVertex2f(player1.width*16+x*window_coordinates + x_step,y+player1.height*0+y*window_coordinates + y_step)
  glEnd()

  glColor3f(0,0,0)
  glBegin(GL_TRIANGLES)
  glVertex2f(player1.width*11+x*window_coordinates + x_step,y+player1.height*1+y*window_coordinates + y_step)
  glVertex2f(player1.width*6+x*window_coordinates + x_step,y+player1.height*2+y*window_coordinates + y_step)
  glVertex2f(player1.width*6+x*window_coordinates + x_step,y+player1.height*0+y*window_coordinates + y_step)
  glEnd()

def DesenhaPlayer2(x, y, x_step=0, y_step=0):
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width/5))
    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width*0.70))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.80),y*window_coordinates + y_step + (player2.width*0.70))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.80),y*window_coordinates + y_step + (player2.width/5))
    glEnd()
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.52),y*window_coordinates + y_step + (player2.width/5))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.52),y*window_coordinates + y_step + (player2.width*0.75))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.78),y*window_coordinates + y_step + (player2.width*0.75))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.78),y*window_coordinates + y_step + (player2.width/5))
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.55),y*window_coordinates + y_step + (player2.width/5))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.55),y*window_coordinates + y_step + (player2.width*0.80))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.75),y*window_coordinates + y_step + (player2.width*0.80))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.75),y*window_coordinates + y_step + (player2.width/5))
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.57),y*window_coordinates + y_step + (player2.width*0.60))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.57),y*window_coordinates + y_step + (player2.width*0.65))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.62),y*window_coordinates + y_step + (player2.width*0.65))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.62),y*window_coordinates + y_step + (player2.width*0.60))
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.57),y*window_coordinates + y_step + (player2.width*0.65))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.63),y*window_coordinates + y_step + (player2.width*0.68))
    glEnd()

    glColor3f(1,1,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width*0.55))
    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width*0.70))
    glVertex2f(x*window_coordinates + x_step + (player2.width/5),y*window_coordinates + y_step + (player2.width/2))
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(x*window_coordinates + x_step + (player2.width/5),y*window_coordinates + y_step + (player2.width/2))
    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width*0.60))
    glEnd()

    glColor3f(0.8,0.4,0)
    glBegin(GL_POLYGON)
    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width/5))
    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width/2))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.55),y*window_coordinates + y_step + (player2.width*0.55))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.59),y*window_coordinates + y_step + (player2.width/2))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.63),y*window_coordinates + y_step + (player2.width*0.55))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.67),y*window_coordinates + y_step + (player2.width/2))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.71),y*window_coordinates + y_step + (player2.width*0.55))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.75),y*window_coordinates + y_step + (player2.width/2))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.79),y*window_coordinates + y_step + (player2.width*0.55))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.80),y*window_coordinates + y_step + (player2.width/2))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.80),y*window_coordinates + y_step + (player2.width/5))
    glEnd()

    glColor(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width/5))
    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width*0.55))

    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width*0.55))
    glVertex2f(x*window_coordinates + x_step + (player2.width/5),y*window_coordinates + y_step + (player2.width/2))

    glVertex2f(x*window_coordinates + x_step + (player2.width/5),y*window_coordinates + y_step + (player2.width/2))
    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width*0.70))

    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width*0.70))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.52),y*window_coordinates + y_step + (player2.width*0.70))

    glVertex2f(x*window_coordinates + x_step + (player2.width*0.52),y*window_coordinates + y_step + (player2.width*0.70))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.52),y*window_coordinates + y_step + (player2.width*0.75))

    glVertex2f(x*window_coordinates + x_step + (player2.width*0.52),y*window_coordinates + y_step + (player2.width*0.75))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.55),y*window_coordinates + y_step + (player2.width*0.75))

    glVertex2f(x*window_coordinates + x_step + (player2.width*0.55),y*window_coordinates + y_step + (player2.width*0.75))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.55),y*window_coordinates + y_step + (player2.width*0.80))

    glVertex2f(x*window_coordinates + x_step + (player2.width*0.55),y*window_coordinates + y_step + (player2.width*0.80))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.75),y*window_coordinates + y_step + (player2.width*0.80))

    glVertex2f(x*window_coordinates + x_step + (player2.width*0.75),y*window_coordinates + y_step + (player2.width*0.80))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.75),y*window_coordinates + y_step + (player2.width*0.75))

    glVertex2f(x*window_coordinates + x_step + (player2.width*0.75),y*window_coordinates + y_step + (player2.width*0.75))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.78),y*window_coordinates + y_step + (player2.width*0.75))

    glVertex2f(x*window_coordinates + x_step + (player2.width*0.78),y*window_coordinates + y_step + (player2.width*0.75))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.78),y*window_coordinates + y_step + (player2.width*0.70))

    glVertex2f(x*window_coordinates + x_step + (player2.width*0.78),y*window_coordinates + y_step + (player2.width*0.70))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.80),y*window_coordinates + y_step + (player2.width*0.70))

    glVertex2f(x*window_coordinates + x_step + (player2.width*0.80),y*window_coordinates + y_step + (player2.width*0.70))
    glVertex2f(x*window_coordinates + x_step + (player2.width*0.80),y*window_coordinates + y_step + (player2.width/5))

    glVertex2f(x*window_coordinates + x_step + (player2.width*0.80),y*window_coordinates + y_step + (player2.width/5))
    glVertex2f(x*window_coordinates + x_step + (player2.width/2),y*window_coordinates + y_step + (player2.width/5))
    glEnd()

def DesenhaBola(width, height, x, y, x_step = 0, y_step = 0, red=0):
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t, points, radius
  if red:
    glBegin(GL_POLYGON)
    glColor3f(0,0,1)
    for i in range(points):
        cos = red_ball.radius * np.cos(i * 2 * np.pi / points) + x*window_coordinates + x_step
        sin = 1.5*red_ball.radius * np.sin(i * 2 * np.pi / points) + y*window_coordinates + y_step
        glVertex2f(cos, sin)
    glEnd()

    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(1.8*red_ball.radius - 2*red_ball.radius + x*window_coordinates + x_step,3.5*red_ball.radius- 2*red_ball.radius+y*window_coordinates + y_step)
    glVertex2f(2.2*red_ball.radius- 2*red_ball.radius+ x*window_coordinates + x_step,3.5*red_ball.radius- 2*red_ball.radius+y*window_coordinates + y_step)
    glVertex2f(2.2*red_ball.radius- 2*red_ball.radius+ x*window_coordinates + x_step,.5*red_ball.radius- 2*red_ball.radius+y*window_coordinates + y_step)
    glVertex2f(1.8*red_ball.radius- 2*red_ball.radius+ x*window_coordinates + x_step,.5*red_ball.radius- 2*red_ball.radius+y*window_coordinates + y_step)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(red_ball.radius- 2*red_ball.radius+ x*window_coordinates + x_step,1.8*red_ball.radius- 2*red_ball.radius+y*window_coordinates + y_step)
    glVertex2f(red_ball.radius- 2*red_ball.radius+ x*window_coordinates + x_step,2.2*red_ball.radius- 2*red_ball.radius+y*window_coordinates + y_step)
    glVertex2f(3*red_ball.radius- 2*red_ball.radius+ x*window_coordinates + x_step,2.2*red_ball.radius- 2*red_ball.radius+y*window_coordinates + y_step)
    glVertex2f(3*red_ball.radius- 2*red_ball.radius+ x*window_coordinates + x_step,1.8*red_ball.radius- 2*red_ball.radius+y*window_coordinates + y_step)
    glEnd()
   

  else:
    glColor3f(.5, .5, .5)

    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    for i in range(points):
        cos = ball.radius * np.cos(i * 2 * np.pi / points) + x*window_coordinates + x_step
        sin = 1.5*ball.radius * np.sin(i * 2 * np.pi / points) + y*window_coordinates + y_step
        glVertex2f(cos, sin)
    glEnd()

def Desenha():
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t
  
  glClear(GL_COLOR_BUFFER_BIT)
  
  glViewport(0,0,window_width,window_height)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(0,300,0,250)
  
  Background()

  glViewport(0,0,window_width,window_height)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-window_coordinates,window_coordinates,-window_coordinates,window_coordinates)

  DesenhaObjeto(window_coordinates, 10, 0,1)
  DesenhaObjeto(window_coordinates, 10, 0,-1)

  DesenhaPlayer1(player1.x, player1.y)
  DesenhaPlayer2(player2.x, player2.y)

  DesenhaTexto(string = str(player1.score), pos = 0)
  DesenhaTexto(string = str(player2.score), pos= 1)
  
  DesenhaBola(5, 5, red_ball.x,red_ball.y, red=1)
  DesenhaBola(5, 5, ball.x,ball.y)

  DesenhaTexto(string = f"{remaining_time:.1f}", pos = 2)
  
  glutSwapBuffers()

def Timer(value):
  global player1, player2, ball, red_ball, window_height, window_width, window_coordinates, pause_game, end_game, game_time_limit, remaining_time, hold_time, reset_time, timer_red, delta_time_red
  t = glutGet(GLUT_ELAPSED_TIME) - reset_time
  delta_time_red = t - timer_red

  if  game_time_limit - (t/1000 - hold_time) <= 0:
    if player1.score > player2.score : 
      resultado = "Ganhador: Player 1"
    elif player1.score < player2.score : 
      resultado = "Ganhador: Player 2"
    else:
      resultado = "Empate"
    DesenhaTexto(string = f"Fim de jogo.", result = resultado)
    glutSwapBuffers()
    pause_game = True
    end_game = True
  remaining_time = game_time_limit - (t/1000 - hold_time)
  
  if not pause_game:
    if delta_time_red > 500:
      glClearColor(0.3, 0.8, 1, 1)

    if ball.x < 0:
        if (abs(ball.x) + abs(ball.xstep) >= 1-player_width/100) and (abs(ball.y) < abs(player1.y) + abs(player1.height*0.1) and abs(ball.y) > abs(player1.y) - abs(player1.height*0.05) ):
          ball.xstep *= -1.25
          red_ball.xstep *= 1.15
          ball.x += .1

    if ball.x > 0:
        if (abs(ball.x) + ball.xstep >= 1-player_width/100) and (abs(ball.y) < abs(player2.y) + player2.height*0.1 and abs(ball.y) > abs(player2.y) - player2.height*0.1 ):
          ball.xstep *= -1.25
          red_ball.xstep *= 1.15
          ball.x -= .075
    
    if abs(ball.y*window_coordinates) > window_coordinates-20:
      ball.ystep *= -1

    if abs(ball.x*window_coordinates) > window_coordinates:
      
      if ball.x > 0:
        player1.score += 1
      else:
        player2.score += 1
        glClearColor(1, 0, 0, 1)
        timer_red = t


      ball = Ball(0,0,5,0.015)
      red_ball = Ball(0,0,5,0.025)
      
    ball.x += ball.xstep
    ball.y += ball.ystep
    
    glutPostRedisplay()
    glutTimerFunc(33, Timer, 1)

def TimerRed(value):
  global player1, player2, ball, red_ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t

  if not pause_game:
    if red_ball.x < 0:        
        if (abs(red_ball.x) + abs(red_ball.xstep) >= 1-player_width/100) and (red_ball.y < player1.y + player1.height*0.1 and red_ball.y > player1.y - player1.height*0.05 ):                    
          player1.score -= 1
          red_ball = Ball(0,0,5,0.025)
    if red_ball.x > 0:        
        if (abs(red_ball.x) + red_ball.xstep >= 1-player_width/100) and (red_ball.y < player2.y + player2.height*0.1 and red_ball.y > player2.y - player2.height*0.05 ):                    
          player2.score -= 1
          red_ball = Ball(0,0,5,0.025)
    
    if abs(red_ball.y*window_coordinates) > window_coordinates-20:
      red_ball.ystep *= -1

    if abs(red_ball.x*window_coordinates) > window_coordinates:
      old_red_ball_speed = red_ball.ball_speed * 1.25
      red_ball = Ball(0,0,5,old_red_ball_speed)

    red_ball.x += red_ball.xstep
    red_ball.y += red_ball.ystep
    
    glutPostRedisplay()
    glutTimerFunc(33, TimerRed, 1)

def HandleMenu(op):
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, end_game, game_time_limit, remaining_time, hold_time, reset_time
  match op:
    case 0:
      if not pause_game:
        hold_time += glutGet(GLUT_ELAPSED_TIME) / 1000
        pause_game = True
    case 1:
      if pause_game and not end_game:
        hold_time = glutGet(GLUT_ELAPSED_TIME) / 1000 - hold_time
        pause_game = False
        glutTimerFunc(33, Timer, 1)
        glutTimerFunc(33, TimerRed, 1)    
    case 2:
      player1.score = 0
      player2.score = 0

      reset_time = glutGet(GLUT_ELAPSED_TIME)
      remaining_time = game_time_limit
      hold_time = 0      

      ball.x, ball.y = 0,0
      ball.ball_speed = 0.035
      ball.xstep = ball.ball_speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -ball.ball_speed*np.cos(np.pi/4)
      y_direction = random.choice([np.pi/(i/10) for i in range(25,60)])
      ball.ystep = ball.ball_speed*np.sin(y_direction) if random.randint(0,1) == 1 else -ball.ball_speed*(np.sin(y_direction))
    
      red_ball.x, red_ball.y = 0,0
      red_ball.ball_speed = 0.035
      red_ball.xstep = red_ball.ball_speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -red_ball.ball_speed*np.cos(np.pi/4)
      y_direction = random.choice([np.pi/(i/10) for i in range(25,60)])
      red_ball.ystep = red_ball.ball_speed*np.sin(y_direction) if random.randint(0,1) == 1 else -red_ball.ball_speed*(np.sin(y_direction))
      
      if pause_game:
        end_game = False
        pause_game = False
        glutTimerFunc(33, Timer, 1)
        glutTimerFunc(33, TimerRed, 1)    
    case -1:
      glutLeaveMainLoop()

  return 0

def CriaMenu():
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t
  glutCreateMenu(HandleMenu)
  glutAddMenuEntry("Pausar", 0)
  glutAddMenuEntry("Voltar", 1)
  glutAddMenuEntry("Reiniciar", 2)
  glutAddMenuEntry("Sair", -1)
  glutAttachMenu(GLUT_RIGHT_BUTTON)

def Teclado(key, x, y):
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t
  if key == b'\x08':
    glutLeaveMainLoop()

  if not pause_game:
    match key:
      case b"w":
        if player1.y + 0.2 < 1 - ( player1.height / window_coordinates ):
          player1.y += .2
      case b"s":
        if player1.y - 0.2 >  -1.2 + ( player1.height / window_coordinates ):
          player1.y -= .2
      case 101:
        if player2.y + 0.2 < 1 - ( player2.height / window_coordinates ):
          player2.y += .2
      case 103:
        if player2.y - 0.2 > -1.2 + ( player2.height / window_coordinates ):
          player2.y -= .2
 
    glutPostRedisplay()     

def Responsivo(width, height):
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t
  window_width = width
  window_height = height

def DesenhaTexto(string, result = None, pos = -1):
    glPushMatrix()
    glColor3f(0.0, 0.0, 0.0);
    if pos == 0:
      glRasterPos2f(-25,80)
    elif pos == 1:
      glRasterPos2f(25,80)
    elif pos == 2:
      glRasterPos2f(0,80)
    else:
      glRasterPos2f(-7.5,0)

    if result:
        glRasterPos2f(-7.5,-7.5)
        for char in result:
          glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(char))
        
    else:
      for char in string:     
          glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(char))                                
    
    glPopMatrix()

def main():
  global pause_game
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
  glutInitWindowSize(screensize[0], screensize[1]-80)
  glutInitWindowPosition(0,0)
  glutCreateWindow(b"Uber Loveable Frog")
  #glutFullScreen()
  glutDisplayFunc(Desenha)
  glutReshapeFunc(Responsivo)
  glutSetKeyRepeat(GLUT_KEY_REPEAT_OFF)
  glutKeyboardFunc(Teclado)
  glutSpecialFunc(Teclado)
  glutTimerFunc(33, Timer if not pause_game else lambda:None, 1)
  glutTimerFunc(33, TimerRed if not pause_game else lambda:None, 1)
  CriaMenu()
  glClearColor(0.3, 0.8, 1, 1)
  glutMainLoop()

main()
