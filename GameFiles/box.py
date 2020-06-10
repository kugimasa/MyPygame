import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

move_step = 0.05

vertices = (
    (1,-1,-1),  #0
    (1,1,-1),   #1
    (-1,1,-1),  #2
    (-1,-1,-1), #3
    (1,-1,1),   #4
    (1,1,1),    #5
    (-1,1,1),   #6
    (-1,-1,1)   #7
)

edges = (
    (0,1), 
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,6),
    (7,3),
    (7,4),
    (7,6),
    (5,1),
    (5,4),
    (5,6)
)

#表面
surfaces = (
    (0,3,7,4), #BOTTOM
    (3,2,1,0), #BACK
    (0,1,5,4), #LEFT
    (7,3,2,6), #RIGHT
    (6,5,1,2), #TOP
    (6,7,4,5), #FRONT
)

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1)
)

def Cube():
    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        for vertex in surface:
            if (x > 10):
                x = 0
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()
    
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)
    glRotatef(25,2,1,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            glTranslatef(-move_step,0,0)
        if keys[pygame.K_RIGHT]:
            glTranslatef(move_step,0,0)
        if keys[pygame.K_UP]:
            glTranslatef(0,move_step,0)
        if keys[pygame.K_DOWN]:
            glTranslatef(0,-move_step,0)
            
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        
main()
