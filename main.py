#https://www.youtube.com/watch?v=a4NVQC_2S2U&t=64s&ab_channel=NaseemShah
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random
import numpy as np
from player import Player
from ball import Ball

window_coordinates = 100
player_width = 5
player_height = 10

player1 = Player(-1,0,player_width,player_height)
player2 = Player(1,0,player_width,player_height)

ball = Ball(0,0,5,5,0.035)
red_ball = Ball(0,0,5,5,0.025)

def DesenhaObjeto(width, height, x, y, x_step = 0, y_step = 0):
  global player1, player2, ball, window_height, window_width, window_coordinates

  glColor3f(.5, .5, .5)
  glBegin(GL_QUADS)

  glVertex2f(-1*width + x*window_coordinates + x_step,-1*height + y*window_coordinates + y_step)
  glVertex2f(-1*width + x*window_coordinates + x_step,1*height + y*window_coordinates + y_step)
  glVertex2f(1*width + x*window_coordinates + x_step,1*height + y*window_coordinates + y_step)
  glVertex2f(1*width + x*window_coordinates + x_step,-1*height + y*window_coordinates + y_step)

  glEnd()

def DesenhaBola(width, height, x, y, x_step = 0, y_step = 0, red=0):
  global player1, player2, ball, window_height, window_width, window_coordinates
  if red:
    glColor3f(.75, 0, 0)
  else:
    glColor3f(.5, .5, .5)

  glBegin(GL_QUADS)

  glVertex2f(-1*width + x*window_coordinates + x_step,-1*height + y*window_coordinates + y_step)
  glVertex2f(-1*width + x*window_coordinates + x_step,1*height + y*window_coordinates + y_step)
  glVertex2f(1*width + x*window_coordinates + x_step,1*height + y*window_coordinates + y_step)
  glVertex2f(1*width + x*window_coordinates + x_step,-1*height + y*window_coordinates + y_step)

  glEnd()

def Desenha():
  global player1, player2, ball, window_height, window_width, window_coordinates
  
  glClear(GL_COLOR_BUFFER_BIT)

  glViewport(0,0,window_width,window_height)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-window_coordinates,window_coordinates,-window_coordinates,window_coordinates)
  DesenhaObjeto(player_width, player_height, player1.x, player1.y)
  DesenhaTexto(str(player1.score), 0)
  DesenhaObjeto(player_width, player_height, player2.x,player2.y)
  DesenhaTexto(str(player2.score), 1)
  DesenhaBola(5, 5, red_ball.x,red_ball.y, red=1)
  DesenhaBola(5, 5, ball.x,ball.y)
  glutSwapBuffers()

def Inicializa():
  glClearColor(0,0,0,1)

def Timer(value):
  global player1, player2, ball, window_height, window_width, window_coordinates

  if ball.x < 0:
      if (abs(ball.x) + abs(ball.xstep) >= 1-2*player_width/100) and (ball.y < player1.y + 0.1 and ball.y > player1.y - 0.1 ):
        ball.xstep *= -1.1
        ball.x += .075

  if ball.x > 0:
      if (abs(ball.x) + ball.xstep >= 1-2*player_width/100) and (ball.y < player2.y + 0.1 and ball.y > player2.y - 0.1 ):
        ball.xstep *= -1.1
        ball.x -= .075
  
  if abs(ball.y*window_coordinates) > window_coordinates-10:
    ball.ystep *= -1

  if abs(ball.x*window_coordinates) > window_coordinates:
    
    if ball.x > 0:
      player1.score += 1
    else:
      player2.score += 1

    ball.x, ball.y = 0,0
    ball.speed = 0.035
    ball.xstep = ball.speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -ball.speed*np.cos(np.pi/4)
    y_direction = random.choice([np.pi/(i/10) for i in range(25,60)])
    ball.ystep = ball.speed*np.sin(y_direction) if random.randint(0,1) == 1 else -ball.speed*(np.sin(y_direction))
  
  ball.x += ball.xstep
  ball.y += ball.ystep

  glutPostRedisplay()
  glutTimerFunc(33, Timer, 1)

def TimerRed(value):
  global player1, player2, ball, window_height, window_width, window_coordinates

  if red_ball.x < 0:
      if (abs(red_ball.x) + abs(red_ball.xstep) >= 1-2*player_width/100) and (red_ball.y < player1.y + 0.1 and red_ball.y > player1.y - 0.1 ):
        red_ball.xstep *= -1.1
        red_ball.x += .075
        player1.score -= 1

  if red_ball.x > 0:
      if (abs(red_ball.x) + red_ball.xstep >= 1-2*player_width/100) and (red_ball.y < player2.y + 0.1 and red_ball.y > player2.y - 0.1 ):
        red_ball.xstep *= -1.1
        red_ball.x -= .075
        player2.score -= 1
  
  if abs(red_ball.y*window_coordinates) > window_coordinates-10:
    red_ball.ystep *= -1

  if abs(red_ball.x*window_coordinates) > window_coordinates:
    
    if red_ball.x > 0:
      player1.score += 1
    else:
      player2.score += 1

    red_ball.x, red_ball.y = 0,0
    red_ball.speed = 0.015
    red_ball.xstep = red_ball.speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -red_ball.speed*np.cos(np.pi/4)
    y_direction = random.choice([np.pi/(i/10) for i in range(25,60)])
    red_ball.ystep = red_ball.speed*np.sin(y_direction) if random.randint(0,1) == 1 else -red_ball.speed*(np.sin(y_direction))
  
  red_ball.x += red_ball.xstep
  red_ball.y += red_ball.ystep

  glutPostRedisplay()
  glutTimerFunc(33, TimerRed, 1)

def Teclado(key, x, y):
  global player1, player2, ball, window_height, window_width, window_coordinates
  match key:
    case b"w":
      if player1.y + 0.2 < 1 - ( player_height / window_coordinates ):
        player1.y += .2
    case b"s":
      if player1.y - 0.2 >  -1 + ( player_height / window_coordinates ):
        player1.y -= .2
    case 101:
      if player2.y + 0.2 < 1 - ( player_height / window_coordinates ):
        player2.y += .2
    case 103:
      if player2.y - 0.2 > -1 + ( player_height / window_coordinates ):
        player2.y -= .2
    case b'\x1b':
      glutLeaveMainLoop()

  glutPostRedisplay()

def Responsivo(width, height):
  global player1, player2, ball, window_height, window_width, window_coordinates
  window_width = width
  window_height = height

def DesenhaTexto(string, pos):
    glPushMatrix()

    if not pos:
      glRasterPos2f(-25,90)
    else:
      glRasterPos2f(25,90)

    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(char))
    glPopMatrix()

def main():
  global windows
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
  glutInitWindowPosition(0,0)
  glutCreateWindow(b"Uber Loveable Frog")
  glutFullScreen()
  glutDisplayFunc(Desenha)
  glutReshapeFunc(Responsivo)
  glutSetKeyRepeat(GLUT_KEY_REPEAT_OFF)
  glutKeyboardFunc(Teclado)
  glutSpecialFunc(Teclado)
  glutTimerFunc(33, Timer, 1)
  glutTimerFunc(33, TimerRed, 1)
  Inicializa()
  glutMainLoop()

main()
