#https://www.youtube.com/watch?v=a4NVQC_2S2U&t=64s&ab_channel=NaseemShah
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random
import numpy as np
from player import Player

window_coordinates = 100
player_width = 5
player_height = 10

player1 = Player(-1,0,player_width,player_height)
player2 = Player(1,0,player_width,player_height)

ball_x, ball_y = 0,0

ball_speed = 0.035
ball_xstep = ball_speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -ball_speed*np.cos(np.pi/4)
y_direction = random.choice([np.pi/(i/10) for i in range(25,150)])
ball_ystep = ball_speed*(np.sin(y_direction)) if random.randint(0,1) == 1 else -ball_speed*(np.sin(y_direction))

def DesenhaObjeto(width, height, x, y, x_step = 0, y_step = 0):
  global player1_x, player1_y, player2_x, player2_y, player_width, player_height, ball_xstep, ball_ystep, window_height, window_width, window_coordinates

  glColor3f(.5, .5, .5)
  glBegin(GL_QUADS)

  glVertex2f(-1*width + x*window_coordinates + x_step,-1*height + y*window_coordinates + y_step)
  glVertex2f(-1*width + x*window_coordinates + x_step,1*height + y*window_coordinates + y_step)
  glVertex2f(1*width + x*window_coordinates + x_step,1*height + y*window_coordinates + y_step)
  glVertex2f(1*width + x*window_coordinates + x_step,-1*height + y*window_coordinates + y_step)

  glEnd()


def Desenha():
  global player1_x, player1_y, player2_x, player2_y, player_width, player_height, ball_xstep, ball_ystep, window_height, window_width, window_coordinates
  glClear(GL_COLOR_BUFFER_BIT)

  glViewport(0,0,window_width,window_height)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-window_coordinates,window_coordinates,-window_coordinates,window_coordinates)
  DesenhaObjeto(player_width, player_height, player1.x, player1.y)
  DesenhaTexto(str(player1.score), 0)
  DesenhaObjeto(player_width, player_height, player2.x,player2.y)
  DesenhaTexto(str(player2.score), 1)
  DesenhaObjeto(5, 5, ball_x,ball_y)
  glutSwapBuffers()

def Inicializa():
  glClearColor(0,0,0,1)

def Timer(value):
  global player1, player2, player_width, player_height,ball_x, ball_y, ball_xstep, ball_ystep, window_height, window_width, window_coordinates

  if ball_x < 0:
      if (abs(ball_x) + abs(ball_xstep) >= 1-player_width/100) and (ball_y < player1.y + 0.1 and ball_y > player1.y - 0.1 ):
        ball_xstep *= -1
        ball_x += .075

  if ball_x > 0:
      if (abs(ball_x) + ball_xstep >= 1-player_width/100) and (ball_y < player2.y + 0.1 and ball_y > player2.y - 0.1 ):
        ball_xstep *= -1
        ball_x -= .075
  
  if abs(ball_y*window_coordinates) > window_coordinates-10:
    ball_ystep *= -1

  if abs(ball_x*window_coordinates) > window_coordinates:
    
    if ball_x > 0:
      player1.score += 1
    else:
      player2.score += 1

    ball_x, ball_y = 0,0
    ball_speed = 0.035
    ball_xstep = ball_speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -ball_speed*np.cos(np.pi/4)
    y_direction = random.choice([np.pi/(i/10) for i in range(25,60)])
    ball_ystep = ball_speed*np.sin(y_direction) if random.randint(0,1) == 1 else -ball_speed*(np.sin(y_direction))
  
  ball_x += ball_xstep
  ball_y += ball_ystep

  glutPostRedisplay()
  glutTimerFunc(33, Timer, 1)

def Teclado(key, x, y):
  global player1, player2, player2_y, player_width, player_height, ball_xstep, ball_ystep, window_height, window_width, window_coordinates
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
  global player1_x, player1_y, player2_x, player2_y, player_width, player_height, ball_xstep, ball_ystep, window_height, window_width, window_coordinates
  window_width = width
  window_height = height

def DesenhaTexto(string, pos):
    glPushMatrix()
    print(GL_CURRENT_RASTER_POSITION)
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
  window = glutCreateWindow(b"Uber Loveable Frog")
  glutFullScreen()
  #print(glutGet(GLUT_WINDOW_WIDTH))
  #print(glutGet(GLUT_WINDOW_HEIGHT))
  glutDisplayFunc(Desenha)
  glutReshapeFunc(Responsivo)
  glutSetKeyRepeat(GLUT_KEY_REPEAT_OFF)
  glutKeyboardFunc(Teclado)
  glutSpecialFunc(Teclado)
  glutTimerFunc(33, Timer, 1)
  Inicializa()
  glutMainLoop()

main()
