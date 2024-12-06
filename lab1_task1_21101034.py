from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

W_Width, W_Height = 500,500


ballx = 25
ball1=75
ball2=125
ball3=175
ball4=225
ball5=275
ball6=325
ball7=375
ball8=425
ball9=475
bally =500
ball_a = 500
ball_b =500
ball_c=500
ball_d=500
ball_e =400
ball_f =400
ball_g =400
ball_h =400
ball_i =400
speed = 0.01
ball_size = 6
create_new = False
x_move=0
screen_red=0
screen_blue=0
screen_green=0
def animate():

    glutPostRedisplay()
    global ballx, bally,speed, ball_a, ball_b, ball_c, ball_d, ball_e, ball_f, ball_g, ball_h, ball_i, x_move, ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9

    
    ballx=(ballx+x_move)%500
    ball1=(ball1+x_move)%500
    ball2=(ball2+x_move)%500
    ball3=(ball3+x_move)%500
    ball4=(ball4+x_move)%500
    ball5=(ball5+x_move)%500
    ball6=(ball6+x_move)%500
    ball7=(ball7+x_move)%500
    ball8=(ball8+x_move)%500
    ball9=(ball9+x_move)%500
    
    for i in range(500):
        if bally<250:
            bally=500
        if ball_a<250:
            ball_a=500
        if ball_b<250:
            ball_b=500
        if ball_c<250:
            ball_c=500
        if ball_d<250:
            ball_d=500
        if ball_e<250:
            ball_e=500
        if ball_f<250:
            ball_f=500
        if ball_g<250:
            ball_g=500
        if ball_h<250:
            ball_h=500
        if ball_i<250:
            ball_i=500
        bally=(bally-speed)%500
        ball_a=(ball_a-speed)%500
        ball_b=(ball_b-speed)%500
        ball_c=(ball_c-speed)%500
        ball_d=(ball_d-speed)%500
        ball_e=(ball_e-speed)%500
        ball_f=(ball_f-speed)%500
        ball_g=(ball_g-speed)%500
        ball_h=(ball_h-speed)%500
        ball_i=(ball_i-speed)%500
    

def draw_points(a,b,c,d,e,f,g,h,i,j,k,s):
    glColor3f(0,0,1)
    glPointSize(s) 
    glBegin(GL_POINTS)
    glVertex2f(a,k) 
    glEnd()
    
    glPointSize(s) 
    glBegin(GL_POINTS)
    glVertex2f(b,k)
    glEnd()
    
    glPointSize(s)
    glBegin(GL_POINTS)
    glVertex2f(c,k) 
    glEnd()
    
    glPointSize(s) 
    glBegin(GL_POINTS)
    glVertex2f(d,k) 
    glEnd()
    
    glPointSize(s) 
    glBegin(GL_POINTS)
    glVertex2f(e,k) 
    glEnd()
    
    glPointSize(s) 
    glBegin(GL_POINTS)
    glVertex2f(f,k) 
    glEnd()
    
    glPointSize(s) 
    glBegin(GL_POINTS)
    glVertex2f(g,k)
    glEnd()
    
    glPointSize(s)
    glBegin(GL_POINTS)
    glVertex2f(h,k)
    glEnd()
    
    glPointSize(s) 
    glBegin(GL_POINTS)
    glVertex2f(i,k) 
    glEnd()
    
    glPointSize(s) 
    glBegin(GL_POINTS)
    glVertex2f(j,k) 
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()
    
def specialKeyListener(key, x, y):
    global ballx, ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, x_move

    if key==GLUT_KEY_RIGHT:
        x_move+=0.1
       
    if key== GLUT_KEY_LEFT:	
        x_move-=0.1
        
    glutPostRedisplay()

def draw_house():
    glColor3f(1,0,0)
    glBegin(GL_LINES)
    glVertex2d(100,100)
    glVertex2d(100,300)
    glVertex2d(400,100)
    glVertex2d(400,300)
    glVertex2d(100,100)
    glVertex2d(400,100)
    glVertex2d(50,300)
    glVertex2d(450,300)
    glVertex2d(450,300)
    glVertex2d(250,400)
    glVertex2d(50,300)
    glVertex2d(250,400)
    glVertex2d(300,150)
    glVertex2d(300,200)
    glVertex2d(350,200)
    glVertex2d(350,150)
    glVertex2d(300,150)
    glVertex2d(350,150)
    glVertex2d(300,200)
    glVertex2d(350,200)
    glVertex2d(325,150)
    glVertex2d(325,200)
    glVertex2d(300,175)
    glVertex2d(350,175)
    glVertex2d(150,100)
    glVertex2d(150,200)
    glVertex2d(200,100)
    glVertex2d(200,200)
    glVertex2d(150,200)
    glVertex2d(200,200)
    glEnd()
    
def keyboardListener(key,x,y):

    global screen_red,screen_green,screen_blue
    if key==b'b':
        screen_red+=0.01
        screen_green+=0.01
        screen_blue+=0.01
    if key==b'd':
        screen_red-=0.01
        screen_green-=0.01
        screen_blue-=0.01

    
    

    glutPostRedisplay()
    
def showScreen():
    global screen_red, screen_blue, screen_green
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(screen_red,screen_green,screen_blue,0)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)
    
    global ballx, bally, ball_size
    draw_points(ballx, ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, bally, ball_size)
    draw_house()
    
    glutSwapBuffers()
    
    
    
    glutPostRedisplay()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") 
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMainLoop()