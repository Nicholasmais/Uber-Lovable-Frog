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
screensize = list(screensize)
screensize[1] -= 80

pause_game = True
end_game = False
game_time_limit = 35
remaining_time = game_time_limit
hold_time = 0
reset_time = 0
timer_red = 0
delta_time_red = 0

window_coordinates = 100
player_size = 10
player_width = 1*player_size
player_height = 2*player_size

player1 = Player(-window_coordinates + player_width/2,0,player_width,player_height, "protagonista")
player2 = Player(window_coordinates - player_width/2*1.5,0,1.5*player_width,player_height, "inimigo")

initial_speed = 0.02

ball = Ball(0,0,player_height / 3,initial_speed)
red_ball = Ball(0,0,player_height / 3,0.025, 1)

ball_colision = 0
red_ball_colision = 0

radius = 25
radius2 = 23
radius3 = 2

def Background(x1 = -window_coordinates, y1=0):
    glColor3f(1,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2f(x1+(0),y1+(0))
    glVertex2f(x1+(0),y1+(600))
    glVertex2f(x1+(window_coordinates + 1.5),y1+(600))
    glVertex2f(x1+(window_coordinates + 1.5),y1+(0))
    glEnd()
    
    glColor3f(1,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2f(x1+(496-window_coordinates),y1+(0))
    glVertex2f(x1+(496-window_coordinates),y1+(600))
    glVertex2f(x1+(500-window_coordinates),y1+(600))
    glVertex2f(x1+(500-window_coordinates),y1+(0))
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

    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    for i in range(50):
        cos = radius * np.cos(i * 2 * np.pi / 50) + x1+(250)
        sin = radius * np.sin(i * 2 * np.pi / 50) + y1+(125)
        glVertex2f(cos, sin)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.3,0.8,1)
    for i in range(50):
        cos = radius2 * np.cos(i * 2 * np.pi / 50) + x1+(250)
        sin = radius2 * np.sin(i * 2 * np.pi / 50) + y1+(125)
        glVertex2f(cos, sin)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    for i in range(50):
        cos = radius3 * np.cos(i * 2 * np.pi / 50) + x1+(250)
        sin = radius3 * np.sin(i * 2 * np.pi / 50) + y1+(125)
        glVertex2f(cos, sin)
    glEnd()

def DesenhaObjeto(width, height, x, y, x_step = 0, y_step = 0):
  global player1, player2, ball, screensize,  window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t

  glColor3f(.7, .7, .7)
  glBegin(GL_QUADS)

  glVertex2f(-1*width + x*window_coordinates + x_step,-1*height + y*window_coordinates + y_step)
  glVertex2f(-1*width + x*window_coordinates + x_step,1*height + y*window_coordinates + y_step)
  glVertex2f(1*width + x*window_coordinates + x_step,1*height + y*window_coordinates + y_step)
  glVertex2f(1*width + x*window_coordinates + x_step,-1*height + y*window_coordinates + y_step)

  glEnd()

def Desenha():
  global player1, player2, ball, screensize,  window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t, explosion_x, explosion_y
  
  glClear(GL_COLOR_BUFFER_BIT)
  
  glViewport(0,0,screensize[0], screensize[1])
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(0,300,0,250)
  
  Background()

  glViewport(0,0,screensize[0], screensize[1])
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-130,150,-130,150)

  if timer_red and delta_time_red < 500:
    red_ball._draw_explosion_(explosion_x, explosion_y,window_coordinates= window_coordinates)

  glViewport(0,0,screensize[0], screensize[1])
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-window_coordinates,window_coordinates,-window_coordinates,window_coordinates)

  DesenhaObjeto(window_coordinates, player_size, 0,1)
  DesenhaObjeto(window_coordinates, player_size, 0,-1)

  glViewport(0,0,screensize[0], screensize[1])
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-window_coordinates,window_coordinates,-window_coordinates,window_coordinates)

  player1._draw_player_()
  player2._draw_player_()

  glViewport(0,0,screensize[0], screensize[1])
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluOrtho2D(-window_coordinates,window_coordinates,-window_coordinates,window_coordinates)

  DesenhaTexto(string = str(player1.score), pos = 0)
  DesenhaTexto(string = str(player2.score), pos= 1)
  
  ball._draw_ball_(window_coordinates=window_coordinates)
  red_ball._draw_ball_(window_coordinates=window_coordinates)

  DesenhaTexto(string = f"{remaining_time:.1f}", pos = 2)
  
  glutSwapBuffers()

def Timer(value):
  global player1, player2, ball, red_ball, screensize,  window_coordinates, pause_game, end_game, game_time_limit, remaining_time, hold_time, reset_time, t, timer_red, delta_time_red, ball_colision, red_ball_colision
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
    if ball.x < 0:
        if (abs(ball.x) + abs(ball.xstep) >= 1-player_width/100) and (ball.y - ball.radius/10 < player1.y + player1.height/10 and ball.y  + ball.radius /10 > player1.y - player1.height/10 ):
          ball.xstep = ball_colision/10*abs(ball.xstep) + initial_speed
          ball_colision += 1          
          red_ball.xstep *= 1.15
          ball.x += .1

    if ball.x > 0:
        if (abs(ball.x) + ball.xstep >= 1-player_width/100) and (ball.y < player2.y + player2.height*0.1 and ball.y > player2.y - player2.height ):
          ball.xstep = -(ball_colision/10*abs(ball.xstep) + initial_speed)
          ball_colision += 1        
          red_ball.xstep *= 1.15
          ball.x -= .1
    
    if abs(ball.y*window_coordinates) > window_coordinates-20:
      ball.ystep *= -1

    if abs(ball.x*window_coordinates) > window_coordinates:
      
      if ball.x > 0:
        player1.score += 1
      else:
        player2.score += 1

      ball = Ball(0,0,player_height / 3,initial_speed)

      red_ball = Ball(0,0,3.5,0.025, 1)
      red_ball_colision = 0
      ball_colision = 0
    ball.x += ball.xstep
    ball.y += ball.ystep
    
    glutPostRedisplay()
    glutTimerFunc(33, Timer, 1)

def TimerRed(value):
  global player1, player2, ball, red_ball, screensize,  window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t, timer_red, explosion_x, explosion_y, initial_speed

  if not pause_game:
    if red_ball.x < 0:        
        if (abs(red_ball.x) + abs(red_ball.xstep) >= 1-player_width/100) and (red_ball.y < player1.y + player1.height*0.1 and red_ball.y > player1.y - player1.height*0.05 ):
          player1.score -= 1        
          explosion_x, explosion_y = red_ball.x, red_ball.y
          red_ball = Ball(0,0,3.5,0.025, 1)
          timer_red = t
    if red_ball.x > 0:        
        if (abs(red_ball.x) + red_ball.xstep >= 1-player_width/100) and (red_ball.y < player2.y + player2.height*0.1 and red_ball.y > player2.y - player2.height*0.05 ):
          player2.score -= 1
          explosion_x, explosion_y = red_ball.x+.15, red_ball.y
          red_ball = Ball(0,0,3.5,0.025, 1)
          timer_red = t
    if abs(red_ball.y*window_coordinates) > window_coordinates-20:
      red_ball.ystep *= -1
    if abs(red_ball.x*window_coordinates) > window_coordinates:
      old_red_ball_speed =  red_ball_colision/10*abs(ball.xstep) + initial_speed
      red_ball = Ball(0,0,3.5,old_red_ball_speed, 1)

    red_ball.x += red_ball.xstep
    red_ball.y += red_ball.ystep
    
    glutPostRedisplay()
    glutTimerFunc(33, TimerRed, 1)

def HandleMenu(op):
  global player1, player2, ball, screensize,  window_coordinates, pause_game, end_game, game_time_limit, remaining_time, hold_time, reset_time, initial_speed
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
      ball.ball_speed = initial_speed
      ball.xstep = ball.ball_speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -ball.ball_speed*np.cos(np.pi/4)
      y_direction = random.choice([np.pi/(i/10) for i in range(25,60)])
      ball.ystep = ball.ball_speed*np.sin(y_direction) if random.randint(0,1) == 1 else -ball.ball_speed*(np.sin(y_direction))
    
      red_ball.x, red_ball.y = 0,0
      red_ball.ball_speed = initial_speed
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
  global player1, player2, ball, screensize,  window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t
  glutCreateMenu(HandleMenu)
  glutAddMenuEntry("Pausar", 0)
  glutAddMenuEntry("Voltar", 1)
  glutAddMenuEntry("Reiniciar", 2)
  glutAddMenuEntry("Sair", -1)
  glutAttachMenu(GLUT_RIGHT_BUTTON)

def Teclado(key, x, y):
  global player1, player2, ball, screensize,  window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t
  if key == b'\x08':
    glutLeaveMainLoop()

  if not pause_game:
    match key:
      case b"w":
        if player1.y + 2*player1.height <= 100:
          player1.y += player1.height
      case b"s":
        if player1.y - 2*player1.height >= -100:
          player1.y -= player1.height
      case 101:
        if player2.y + 20 < 100- ( player2.height ):
          player2.y += 20
      case 103:
        if player2.y - 20 > -120 + ( player2.height ):
          player2.y -= 20
 
    glutPostRedisplay()     

def DesenhaTexto(string, result = None, pos = -1):
    glPushMatrix()
    glColor3f(0.0, 0.0, 0.0);
    if pos == 0:
      glRasterPos2f(-25,80)
    elif pos == 1:
      glRasterPos2f(25,80)
    elif pos == 2:
      glRasterPos2f(-3.25,80)
    else:
      glRasterPos2f(-7.5,0)

    if result:
        glRasterPos2f(-15,0)
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
  glutInitWindowSize(screensize[0], screensize[1])
  glutInitWindowPosition(0,0)
  glutCreateWindow(b"Uber Loveable Frog")
  #glutFullScreen()
  glutDisplayFunc(Desenha)
  glutSetKeyRepeat(GLUT_KEY_REPEAT_OFF)
  glutKeyboardFunc(Teclado)
  glutSpecialFunc(Teclado)
  glutTimerFunc(33, Timer if not pause_game else lambda:None, 1)
  glutTimerFunc(33, TimerRed if not pause_game else lambda:None, 1)
  CriaMenu()
  glClearColor(0.3, 0.8, 1, 1)
  glutMainLoop()

main()
