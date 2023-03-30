from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def task2():
    # Точка
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3d(15, 0, 34)
    glVertex2d(0, 1)
    glEnd()

    # Прямокутник
    glBegin(GL_QUADS)
    glColor3d(0, 45, 1)
    glVertex2d(5, 0)
    glVertex2d(5, 5)
    glVertex2d(10, 5)
    glVertex2d(10, 0)
    glEnd()

    # Лінія
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3d(1, 1, 1)
    glVertex2d(1, 1)
    glVertex2d(-3, 8)
    glEnd()

    # Трикутник
    glBegin(GL_TRIANGLES)
    glColor3d(1, 0, 45)
    glVertex2d(-9, 0)

    glVertex2d(-6, -3)

    glVertex2d(3, 0)
    glEnd()

    # Багатокутник
    glBegin(GL_POLYGON)
    glColor3d(0, 3, 0)
    glVertex2d(4, 4)
    glVertex2d(3, 2)
    glVertex2d(2, 4)
    glVertex2d(2, 8)
    glVertex2d(4, 8)
    glEnd()


def task3():
    glLineWidth(1)
    radius=4
    DEG2RAD = 3.14159 / 180
    glBegin(GL_LINE_LOOP)
    glColor3f(1,1,1)
    for i in range(360):
        degInRad = i * DEG2RAD
        glVertex2f(math.cos(degInRad) * radius, math.sin(degInRad) * radius)
    glEnd()

    glLineWidth(1)
    glBegin(GL_LINES)

    glColor3d(1, 1, 1)

    glVertex2d(4, 0)
    glVertex2d(-4, 0)

    glVertex2d(0, 4)
    glVertex2d(0, -4)
    glEnd()

    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3d(1, 1, 1)

    glVertex2d(0, 4)
    glVertex2d(0, 1)

    glVertex2d(0, -4)
    glVertex2d(0, -1)


    glEnd()

def build_projection():
    # Local space (logical coordinates)
    # Transformation (affine)
    glMatrixMode(GL_MODELVIEW) # Select transformation matrix
    glLoadIdentity() # No transformation
    gluLookAt(0,0,10, 0.,0.,0., 0.,1.,0.) # Eye osition and direction
    # Projection
    glMatrixMode(GL_PROJECTION) # Select transformation matrix
    glLoadIdentity()
    glOrtho(-10,10, -10,10, 1,30) # Clipping
    # View port - window region
    glViewport(0,0,500,500)
def set_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0) # Single lighting source
    glLight(GL_LIGHT0, GL_POSITION, (10, 10, -10, 0))
# We Use glColor() to set color with Ambient and Diffuse lighting
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_COLOR_MATERIAL)
# Define the drawing function
def draw_scene():
# Drawing settings
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    build_projection()
    set_lighting()
# Draw shapes
    glColor3f(.10,.4,.48) # Face color
    task3()# Draw shape
    glutSwapBuffers() # Double buffering
# Init GLUT
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
# Create and setup window
glutInitWindowSize(500,500)
glutInitWindowPosition(0,0)
glutCreateWindow("Simple window")
# Init drawing loop
glutDisplayFunc(draw_scene)
# Run the loop
glutMainLoop() # call once