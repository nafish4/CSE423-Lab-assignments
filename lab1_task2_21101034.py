from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random
import time

W_Width, W_Height = 500,500

c_x=0
c_y=0
speed = 1
ball_size = 20
collection=[]
even=0
blink_flag= False
space_flag=not False
class info:
    def __init__(self):
        self.x=0
        self.y=0
        self.red=0
        self.gre=0
        self.blu=0

count = 0

def draw_points(x, y, s):
    global speed, blink_flag,space_flag, count
    if len(collection)==0:
        pass
    else:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0,0,0,0);	#//color black
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for i in range(0, len(collection)):
            x_move=random.randint(-1,1)*speed if space_flag else 0
            y_move=random.randint(-1,1)*speed if space_flag else 0
            point=collection[i]
            x_point=point.x
            y_point=point.y
            red_val=point.red
            green_val=point.gre
            blue_val=point.blu
            glPointSize(s) 
            glBegin(GL_POINTS)
            if blink_flag==True:
                if int(time.time()) % 2 == 0:
                    glColor3f(red_val, green_val, blue_val)
                else:
                    glColor3f(0, 0, 0)
            else:
                glColor3f(red_val, green_val, blue_val)
            glVertex2f(x_point+x_move,y_point+y_move)

            count+=1
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
    global speed
    if key=='w':
        print(1)
    if key==GLUT_KEY_UP:
        speed+=1
        print("Speed Increased")
    if key== GLUT_KEY_DOWN:		
        speed-=1
        print("Speed Decreased")
    glutPostRedisplay()
    
def mouseListener(button, state, x, y):	
    global ball_size, c_x, c_y, blink_flag,collection
    
    if button == GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            blink_flag=not blink_flag

    
    
    if button==GLUT_RIGHT_BUTTON:
        
        c_x=x
        c_y=500-y
        red=round(random.random(),2)
        green=round(random.random(),2)
        blue=round(random.random(),2)
        obj=info()
        obj.x=c_x
        obj.y=c_y
        obj.red=red
        obj.gre=green
        obj.blu=blue
        collection.append(obj)
        print(x,y,red,green,blue)

           
        

    glutPostRedisplay()

def keyboardListener(key,x,y):

    global space_flag
    if key==b' ':
        if space_flag==False:
           space_flag=True
        else:
           space_flag=False
    

    glutPostRedisplay()    
    
def animate():
    glutPostRedisplay() 


def showScreen():
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) 

    
    global  ball_size, c_x, c_y
    
    draw_points(c_x, c_y, ball_size)
    glutSwapBuffers()





glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()