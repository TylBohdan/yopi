from math import cos, sin

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height = 600, 500
zoom_amount = 15
eye_x = 0
eye_y = 0
eye_z = 1
projection_mode = 2
rotate_x = 0
rotate_y = 0
rotate_z = 0
can_mouse_button = False
aX = 0
aY = 0

CUBE_VERTICES = (

    (1, -1, 1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1),
    (1, -1, -1), (1, 1, -1), (1, 1, 1), (1, -1, 1),
    (1, -1, -1), (1, -1, 1), (-1, -1, 1), (-1, -1, -1),
    (-1, -1, 1), (-1, 1, 1), (-1, 1, -1), (-1, -1, -1),
    (-1, -1, -1), (-1, 1, -1), (1, 1, -1), (1, -1, -1),
    (-1, 1, 1), (1, 1, 1), (1, 1, -1), (-1, 1, -1)
)

CUBE_VERTICES_COLORS = [(x, y, z) for x, y, z in CUBE_VERTICES]

def normal_keys(key, x, y):
    global projection_mode
    if ord(key) == 27:
        glutLeaveMainLoop()

    if ord(key) == 74:
        projection_mode = 1

    if ord(key) == 75:
        projection_mode = 2

    if ord(key) == 76:
        projection_mode = 0

    glutPostRedisplay()

def special_key_input(key, x, y):
    global rotate_x, rotate_y, rotate_z
    global eye_x, eye_y, eye_z
    if key == GLUT_KEY_RIGHT:
        rotate_z += 0.001
        rotate_x += 0.001

    elif key == GLUT_KEY_LEFT:
        rotate_z -= 0.001
        rotate_x -= 0.001

    elif key == GLUT_KEY_UP:
        rotate_z += 0.001
        rotate_y += 0.001

    elif key == GLUT_KEY_DOWN:
        rotate_z -= 0.001
        rotate_y -= 0.001

    eye_x = sin(rotate_x * 180 / 3.1415)
    eye_y = sin(rotate_y * 180 / 3.1415)
    eye_z = cos(rotate_z * 360 / 3.1415)

    glutPostRedisplay()

def mouse_button(button, state, x, y):
    global can_mouse_button, aX, aY
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            can_mouse_button = True
            aX = x
            aY = y
        else:
            can_mouse_button = False

def mouse_move(x, y):
    global rotate_x, rotate_y, rotate_z
    global eye_x, eye_y, eye_z
    if can_mouse_button:
        x_rotate = (x - aX)
        y_rotate = (y - aY)

        if x_rotate > 0:
            rotate_z += 0.0001
            rotate_x += 0.0001
        elif x_rotate < 0:
            rotate_z -= 0.0001
            rotate_x -= 0.0001

        if y_rotate > 0:
            rotate_z += 0.0001
            rotate_y += 0.0001
        elif y_rotate < 0:
            rotate_z -= 0.0001
            rotate_y -= 0.0001

        eye_x = sin(rotate_x * 180 / 3.1415)
        eye_y = sin(rotate_y * 180 / 3.1415)
        eye_z = cos(rotate_z * 360 / 3.1415)

        glutPostRedisplay()

def init_matrix():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if projection_mode == 1:
        glFrustum(-0.7, 0.7, -0.7, 0.7, 0.4, 1000)  # перспективна проекція

    if projection_mode == 2:
        glOrtho(-3, 3, -3, 3, 0.1, 1000)  # паралельна проекція

    value = 1
    if eye_x == 0:
        if eye_y < 0:
            value = -1
        if eye_z == 0:
            value = 0
        if eye_z > 0:
            value = 1

    gluLookAt(eye_x+2, eye_y+2, eye_z+2, 0, 0, 0, 0, value, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def vertices():
    glBegin(GL_QUADS)

    for color, vertex in zip(CUBE_VERTICES_COLORS, CUBE_VERTICES):
        glColor3f(*color)
        glVertex3f(*vertex)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init_matrix()
    glPushMatrix()

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glLineWidth(3)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    vertices()

    glClearDepthf(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)

    glPopMatrix()
    glutSwapBuffers()

def refresh_display():
    glutPostRedisplay()

def reshape(w: int, h: int):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(650, 225)
    glutCreateWindow("OpenGL blank window")
    glClearColor(0.168, 0.196, 0.219, 1)
    glutDisplayFunc(display)
    glutIdleFunc(refresh_display)
    glutReshapeFunc(reshape)

    glutKeyboardFunc(normal_keys)
    glutSpecialFunc(special_key_input)

    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_move)

    glutMainLoop()

if __name__ == "__main__":
    main()