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

end_game = False
pause_game = False
game_time_limit = 15
remaining_time = game_time_limit
hold_time = 0
reset_time = 0

window_coordinates = 100
player_width = 5
player_height = 10

player1 = Player(-1,0,player_width/10,player_width*3/10)
player2 = Player(1,0,player_width,player_height)

points = 50

ball = Ball(0,0,5,0.035)
red_ball = Ball(0,0,5,0.025)

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

def DesenhaBola(width, height, x, y, x_step = 0, y_step = 0, red=0):
  global player1, player2, ball, window_height, window_width, window_coordinates, pause_game, game_time_limit, remaining_time, hold_time, t, points, radius
  if red:
    glBegin(GL_POLYGON)
    glColor3f(0,0,1)
    for i in range(points):
        cos = red_ball.radius * np.cos(i * 2 * np.pi / points) + x*window_coordinates + x_step
        sin = red_ball.radius * np.sin(i * 2 * np.pi / points) + y*window_coordinates + y_step
        glVertex2f(cos, sin)
    glEnd()

    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(1.8*red_ball.radius - 2*red_ball.radius + x*window_coordinates + x_step,3*red_ball.radius- 2*red_ball.radius+y*window_coordinates + y_step)
    glVertex2f(2.2*red_ball.radius- 2*red_ball.radius+ x*window_coordinates + x_step,3*red_ball.radius- 2*red_ball.radius+y*window_coordinates + y_step)
    glVertex2f(2.2*red_ball.radius- 2*red_ball.radius+ x*window_coordinates + x_step,red_ball.radius- 2*red_ball.radius+y*window_coordinates + y_step)
    glVertex2f(1.8*red_ball.radius- 2*red_ball.radius+ x*window_coordinates + x_step,red_ball.radius- 2*red_ball.radius+y*window_coordinates + y_step)
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
  gluOrtho2D(-window_coordinates,window_coordinates,-window_coordinates,window_coordinates)
  
  DesenhaPlayer1(player1.x, player1.y)
  DesenhaObjeto(player_width, player_height, player2.x,player2.y)
  DesenhaTexto(string = str(player1.score), pos = 1)
  DesenhaTexto(string = str(player2.score), pos= 0)
  
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
          ball.xstep *= -1.25
          ball.x += .075

    if ball.x > 0:
        if (abs(ball.x) + ball.xstep >= 1-2*player_width/100) and (ball.y < player2.y + 0.1 and ball.y > player2.y - 0.1 ):
          ball.xstep *= -1.25
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
          red_ball.xstep *= -1.25
          red_ball.x += .075
          player1.score -= 1

    if red_ball.x > 0:
        if (abs(red_ball.x) + red_ball.xstep >= 1-2*player_width/100) and (red_ball.y < player2.y + 0.1 and red_ball.y > player2.y - 0.1 ):
          red_ball.xstep *= -1.25
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

    if result:
        glRasterPos2f(-7.5,-7.5)
        for char in result:
          glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(char))
        
    else:
      for char in string:          
          glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(char))
          if pos == 0:
            print(str(player1.score),char, pos)
            print("")
    
    glPopMatrix()

def main():
  global windows
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
  glutInitWindowSize(int(screensize[0]/4)-100, int(screensize[1]/4)-100)
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
