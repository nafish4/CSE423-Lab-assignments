from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

center=[]
radius=[]
arr=[]
d=0
c_y=0
c_x=0
limit=False
temp=0
speed=0.05
pause=False
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()
    
def mouseListener(button, state, x, y):	
    global pause
    if button == GLUT_RIGHT_BUTTON and pause==False:
        if(state == GLUT_DOWN):
            print("True")
            center.append((x,500-y))
            radius.append(16)

def draw():
    global d,c_y,c_x,arr,limit,temp,speed
    arr=[]
    for i in range(len(radius)):
        
        c_y=radius[i]
        d=1-c_y
        c_x=0
        while c_x<c_y:
            if d<0:
                d=d+(2*c_x)+3
                c_x+=1
            else:
                d=d+(2*c_x)-(2*c_y)+5
                c_x+=1
                c_y-=1
            if c_x+center[i][0]>500 or c_y+center[i][1]>500 or c_y+center[i][1]<0 or c_x+center[i][0]<0:
                limit=True
            if c_x+center[i][0]>500 or -c_y+center[i][1]>500 or -c_y+center[i][1]<0 or c_x+center[i][0]<0:
                limit=True
            if -c_x+center[i][0]>500 or -c_y+center[i][1]>500 or -c_y+center[i][1]<0 or -c_x+center[i][0]<0:
                limit=True
            if -c_x+center[i][0]>500 or c_y+center[i][1]>500 or c_y+center[i][1]<0 or -c_x+center[i][0]<0:
                limit=True
            if c_y+center[i][0]>500 or c_x+center[i][1]>500 or c_x+center[i][1]<0 or c_y+center[i][0]<0:
                limit=True
            if -c_y+center[i][0]>500 or c_x+center[i][1]>500 or c_x+center[i][1]<0 or -c_y+center[i][0]<0:
                limit=True
            if -c_y+center[i][0]>500 or -c_x+center[i][1]>500 or -c_x+center[i][1]<0 or -c_y+center[i][0]<0:
                limit=True
            if c_y+center[i][0]>500 or -c_x+center[i][1]>500 or -c_x+center[i][1]<0 or c_y+center[i][0]<0:
                limit=True
            if limit==False:
                arr.append((c_x+center[i][0],c_y+center[i][1]))
                arr.append((c_x+center[i][0],-c_y+center[i][1]))
                arr.append((-c_x+center[i][0],-c_y+center[i][1]))
                arr.append((-c_x+center[i][0],c_y+center[i][1]))
                arr.append((c_y+center[i][0],c_x+center[i][1]))
                arr.append((-c_y+center[i][0],c_x+center[i][1]))
                arr.append((-c_y+center[i][0],-c_x+center[i][1]))
                arr.append((c_y+center[i][0],-c_x+center[i][1]))
            else:
                radius.pop(i)
                center.pop(i)
                print(radius)
                break
        if limit==False:
            for x,y in arr:
                glPointSize(1) 
                glBegin(GL_POINTS)
                glVertex2f(x,y)
                glEnd()
            if pause==False:
                temp=radius[i]
                temp+=speed
                radius[i]=temp
        else:
            limit=False
            break
        

def keyboardListener(key,x,y):
    global pause
    if key==b' ' and pause==False:
        
        pause=True
        print("T")
    elif key==b' ' and pause==True:
        pause=False
        print("F")

def specialKeyListener(key, x, y):
    global speed
    if key==GLUT_KEY_LEFT:
        speed+=0.05
        print("true and ")
    if key==GLUT_KEY_RIGHT:
        speed-=0.05
        print("true and ")
def showScreen():
    global pause
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0)
    glLoadIdentity()
    iterate()
    
    draw()
   
    glutSwapBuffers()











glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") 
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)   

glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)
glutMainLoop()