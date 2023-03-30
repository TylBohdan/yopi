from OpenGL.GL import *
from OpenGL.GLUT import *

EscKeyCode = 27
width, height = 600, 500
zoom_amount = 15
angle_x = 0
angle_y = 90
angle_z = 0
can_mouse_move = False


def keydown_input(key, x, y):
    if ord(key) == EscKeyCode:
        glutLeaveMainLoop()


def special_keydown_input(key, x, y):
    if key == GLUT_KEY_LEFT:
        glRotate(3, 0, 1, 0)
    if key == GLUT_KEY_RIGHT:
        glRotate(3, 0, -1, 0)

    if key == GLUT_KEY_UP:
        glRotate(3, 1, 0, 0)
    if key == GLUT_KEY_DOWN:
        glRotate(3, -1, 0, 0)


# zoom with mouse wheel
def mouse_wheel_control(wheel, direction, x, y):
    global zoom_amount
    if direction == -1 and zoom_amount < 25:
        zoom_amount += 1

    elif direction == 1 and zoom_amount > 10:
        zoom_amount -= 1


def mouse_move(x, y):
    global can_mouse_move, angle_x, angle_y
    if can_mouse_move:
        angle_x = -y/4
        angle_y = x/4
    glutPostRedisplay()


def mouse_input(button, state, x, y):
    global can_mouse_move
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            can_mouse_move = True
        else:
            can_mouse_move = False


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    glRotatef(angle_x, 1, 0, 0)
    glRotatef(angle_y, 0, 1, 0)
    glRotatef(angle_z, 0, 0, 1)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glLineWidth(3)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    # zoom viewport setter
    glOrtho(-zoom_amount, zoom_amount,
            -zoom_amount, zoom_amount,
            -zoom_amount, zoom_amount)

    # depth test to avoid translucent mesh
    glClearDepthf(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)

    # display default mesh
    vertices()

    # display mesh wireframe
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glColor3f(0, 0, 0)
    vertices_colorless()

    glPopMatrix()
    glutSwapBuffers()


def vertices():
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex3f(-5, 5, -5)
    glVertex3f(-5, -5, -5)
    glVertex3f(5, -5, -5)
    glVertex3f(5, 5, -5)

    glVertex3f(5, 5, -5)
    glVertex3f(5, -5, -5)
    glVertex3f(5, -5, 5)
    glVertex3f(5, 5, 5)

    glVertex3f(5, 5, 5)
    glVertex3f(5, -5, 5)
    glVertex3f(-5, -5, 5)
    glVertex3f(-5, 5, 5)

    glVertex3f(-5, 5, 5)
    glVertex3f(-5, -5, 5)
    glVertex3f(-5, -5, -5)
    glVertex3f(-5, 5, -5)

    glVertex3f(5, -5, -5)
    glVertex3f(5, -5, 5)
    glVertex3f(-5, -5, 5)
    glVertex3f(-5, -5, -5)

    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 15, 0)
    glVertex3f(5, 5, -5)

    glVertex3f(-5, 5, 5)
    glVertex3f(0, 15, 0)
    glVertex3f(5, 5, 5)

    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 15, 0)

    glVertex3f(-5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 15, 0)

    glEnd()

def vertices_colorless():
    glColor3f(0, 0, 0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glLineWidth(3)

    glBegin(GL_QUADS)
    glVertex3f(-5, 5, -5)
    glVertex3f(-5, -5, -5)
    glVertex3f(5, -5, -5)
    glVertex3f(5, 5, -5)

    glVertex3f(5, 5, -5)
    glVertex3f(5, -5, -5)
    glVertex3f(5, -5, 5)
    glVertex3f(5, 5, 5)

    glVertex3f(5, 5, 5)
    glVertex3f(5, -5, 5)
    glVertex3f(-5, -5, 5)
    glVertex3f(-5, 5, 5)

    glVertex3f(-5, 5, 5)
    glVertex3f(-5, -5, 5)
    glVertex3f(-5, -5, -5)
    glVertex3f(-5, 5, -5)

    glVertex3f(5, -5, -5)
    glVertex3f(5, -5, 5)
    glVertex3f(-5, -5, 5)
    glVertex3f(-5, -5, -5)

    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 15, 0)
    glVertex3f(5, 5, -5)

    glVertex3f(-5, 5, 5)
    glVertex3f(0, 15, 0)
    glVertex3f(5, 5, 5)

    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 15, 0)

    glVertex3f(-5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 15, 0)

    glEnd()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def refresh_display():
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(650, 225)
    glutCreateWindow("OpenGL")
    glClearColor(0, 0.15, 0.25, 1)
    glutDisplayFunc(display)
    glutIdleFunc(refresh_display)
    glutReshapeFunc(reshape)

    glutKeyboardFunc(keydown_input)
    glutMouseWheelFunc(mouse_wheel_control)
    glutSpecialFunc(special_keydown_input)
    glutMotionFunc(mouse_move)
    glutMouseFunc(mouse_input)

    glutMainLoop()


if __name__ == "__main__":
    main()