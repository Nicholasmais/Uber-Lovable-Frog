#https://www.youtube.com/watch?v=a4NVQC_2S2U&t=64s&ab_channel=NaseemShah
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random

player1_x, player1_y = -1, 0
player2_x, player2_y = 1, 0

player_width = 5
player_height = 10

windowWidth = random.randint(100,1000)
windowHeight = random.randint(100,1000)

ball_x, ball_y = 0,0

ball_xstep = windowWidth / 10000
ball_ystep = windowHeight / 20000


window_coordinates = 100

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
  DesenhaObjeto(10, 10, player1_x, player1_y)
  DesenhaObjeto(10, 10, player2_x,player2_y)
  DesenhaObjeto(5, 5, ball_x,ball_y)
  glutSwapBuffers()

def Inicializa():
  glClearColor(0,0,0,1)

def Timer(value):
  global player1_x, player1_y, player2_x, player2_y, player_width, player_height,ball_x, ball_y, ball_xstep, ball_ystep, window_height, window_width, window_coordinates

  if abs(ball_x*window_coordinates) > window_coordinates-1:
    ball_xstep *= -1

  if abs(ball_y*window_coordinates) > window_coordinates-1:
    ball_ystep *= -1

  ball_x += ball_xstep
  ball_y += ball_ystep
  glutPostRedisplay()
  glutTimerFunc(33, Timer, 1)

def Teclado(key, x, y):
  global player1_x, player1_y, player2_x, player2_y, player_width, player_height, ball_xstep, ball_ystep, window_height, window_width, window_coordinates
  match key:
    case b"w":
      y3 += abs(ball_ystep)
    case b"a":
      x3 -= abs(ball_xstep)
    case b"s":
      y3 -= abs(ball_ystep)
    case b"d":
      x3 += abs(ball_xstep)
    
  glutPostRedisplay()

def Responsivo(width, height):
  global player1_x, player1_y, player2_x, player2_y, player_width, player_height, ball_xstep, ball_ystep, window_height, window_width, window_coordinates
  window_width = width
  window_height = height

def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
  glutInitWindowPosition(0,0)
  glutInitWindowSize(windowWidth,windowHeight)
  glutCreateWindow(b"Brasil")
  glutDisplayFunc(Desenha)
  glutReshapeFunc(Responsivo)
  glutKeyboardFunc(Teclado)
  glutTimerFunc(33, Timer, 1)
  Inicializa()
  glutMainLoop()

main()
