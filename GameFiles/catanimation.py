import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
catImg = pygame.image.load('../Assets/cat.png')
catx = 10
caty = 10
direction = 'right'

fontObj = pygame.font.Font('freesansbold.ttf', 28)
textSurfaceObj = fontObj.render('Cat caught!!', True, BLACK, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)
mousex = 0
mousey = 0
catTouch = False

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if catTouch == True:
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    if catTouch == False:
        if direction == 'right':
            catx += 5
            if catx == 280:
                direction = 'down'
        elif direction == 'down':
            caty += 5
            if caty == 220:
                direction = 'left'
        elif direction == 'left':
            catx -= 5
            if catx == 10:
                direction = 'up'
        elif direction == 'up':
            caty -= 5
            if caty == 10:
                direction = 'right'

    CAT = DISPLAYSURF.blit(catImg, (catx, caty))

    #Mouse Handling
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos

    if CAT.collidepoint(mousex, mousey):
        catTouch = True
    else:
        catTouch = False


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
