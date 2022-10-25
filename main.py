#https://www.youtube.com/watch?v=a4NVQC_2S2U&t=64s&ab_channel=NaseemShah
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random
import numpy as np
from player import Player
from ball import Ball

import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

end_game = False
pause_game = False
game_time_limit = 15
remaining_time = game_time_limit
hold_time = 0
reset_time = 0

window_coordinates = 100
player_width = 5
player_height = 10

player1 = Player(-1,0,player_width,player_height)
player2 = Player(1,0,player_width,player_height)

ball = Ball(0,0,5,5,0.035)
red_ball = Ball(0,0,5,5,0.025)

def DesenhaObjeto(width, height, x, y, x_step = 0, y_step = 0):
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t

  glColor3f(.5, .5, .5)
  glBegin(GL_QUADS)

  glVertex2f(-1*width + x*window_coordinates + x_step,-1*height + y*window_coordinates + y_step)
  glVertex2f(-1*width + x*window_coordinates + x_step,1*height + y*window_coordinates + y_step)
  glVertex2f(1*width + x*window_coordinates + x_step,1*height + y*window_coordinates + y_step)
  glVertex2f(1*width + x*window_coordinates + x_step,-1*height + y*window_coordinates + y_step)

  glEnd()

def DesenhaBola(width, height, x, y, x_step = 0, y_step = 0, red=0):
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t
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
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t
  
  glClear(GL_COLOR_BUFFER_BIT)

  glViewport(0,0,window_width,window_height)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-window_coordinates,window_coordinates,-window_coordinates,window_coordinates)
  
  DesenhaObjeto(player_width, player_height, player1.x, player1.y)
  DesenhaTexto(string = str(player1.score), pos = 0)
  DesenhaObjeto(player_width, player_height, player2.x,player2.y)
  DesenhaTexto(string = str(player2.score), pos= 1)
  
  DesenhaBola(5, 5, red_ball.x,red_ball.y, red=1)
  DesenhaBola(5, 5, ball.x,ball.y)

  DesenhaTexto(string = f"{remaining_time:.1f}", pos = 2)
  glutSwapBuffers()

def Timer(value):
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, end_game, game_time_limit, remaining_time, hold_time, reset_time
  t = glutGet(GLUT_ELAPSED_TIME) - reset_time
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
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t

  if not pause_game:

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
      red_ball.x, red_ball.y = 0,0
      red_ball.speed = 0.015
      red_ball.xstep = red_ball.speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -red_ball.speed*np.cos(np.pi/4)
      y_direction = random.choice([np.pi/(i/10) for i in range(25,60)])
      red_ball.ystep = red_ball.speed*np.sin(y_direction) if random.randint(0,1) == 1 else -red_ball.speed*(np.sin(y_direction))

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
      ball.speed = 0.035
      ball.xstep = ball.speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -ball.speed*np.cos(np.pi/4)
      y_direction = random.choice([np.pi/(i/10) for i in range(25,60)])
      ball.ystep = ball.speed*np.sin(y_direction) if random.randint(0,1) == 1 else -ball.speed*(np.sin(y_direction))
    
      red_ball.x, red_ball.y = 0,0
      red_ball.speed = 0.035
      red_ball.xstep = red_ball.speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -red_ball.speed*np.cos(np.pi/4)
      y_direction = random.choice([np.pi/(i/10) for i in range(25,60)])
      red_ball.ystep = red_ball.speed*np.sin(y_direction) if random.randint(0,1) == 1 else -red_ball.speed*(np.sin(y_direction))

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
 
    glutPostRedisplay()     

def Responsivo(width, height):
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t
  window_width = width
  window_height = height

def DesenhaTexto(string, result = None, pos = -1):
    glPushMatrix()

    if pos == 0:
      glRasterPos2f(-25,90)
    elif pos == 1:
      glRasterPos2f(25,90)
    elif pos == 2:
      glRasterPos2f(0,90)
    else:
      glRasterPos2f(-7.5,0)

    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(char))
    
    if result:
        glRasterPos2f(-7.5,-7.5)
        for char in result:
          glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(char))
        
    glPopMatrix()

def main():
  global windows
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
  glutInitWindowSize(screensize[0]-100, screensize[1]-100)
  glutInitWindowPosition(0,0)
  glutCreateWindow(b"Uber Loveable Frog")
  #glutFullScreen()
  glutDisplayFunc(Desenha)
  glutReshapeFunc(Responsivo)
  glutSetKeyRepeat(GLUT_KEY_REPEAT_OFF)
  glutKeyboardFunc(Teclado)
  glutSpecialFunc(Teclado)
  glutTimerFunc(33, Timer, 1)
  glutTimerFunc(33, TimerRed, 1)
  CriaMenu()
  glClearColor(0,0,0,1)
  glutMainLoop()

main()
