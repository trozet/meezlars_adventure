import pygame
from pygame.locals import *
pygame.init()
PLAYERMOVERATE=5
WINDOWWIDTH=640
WINDOWHEIGHT=480
WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0,0,255)

def terminate():
    pygame.quit()
    
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()

            if event.type== KEYDOWN:
                if event.key==K_ESCAPE:
                    terminate()
                return

screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Hello, world!")
background = pygame.Surface(screen.get_size())
background = background.convert()
pygame.image.tostring
#background = pygame.image.load('back.png').convert()
background.fill((44,255,44))
screen.blit(background, (0, 0))
pygame.display.update()
basicFont = pygame.font.SysFont(None, 48)
text=pygame.image.load('back.png').convert()
#text = basicFont.render('You TOOT!', True, WHITE, BLUE)
textRect=text.get_rect()
textRect.centerx=background.get_rect().centerx
textRect.centery=background.get_rect().centery

screen.blit(text, textRect)
pygame.display.update()

#background.fill((44,255,44))
clock = pygame.time.Clock()
moveLeft = moveRight = moveUp = moveDown = False
keepGoing = True
while keepGoing:
    pygame.display.update()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
            terminate()
        if event.type == KEYDOWN:
            print(str(event.key))
            if event.key == ord('a'):
                moveLeft=True
                moveRight=False
            if event.key == ord('d'):
                moveLeft=False
                moveRight=True
            if event.key == ord('w'):
                moveUp=True
                moveDown=False
            if event.key == ord('s'):
                moveUp=False
                moveDown=True
        if event.type == KEYUP:
            print(str(event.key))
            if event.key == ord('a'):
                moveLeft=False
            if event.key == ord('d'):
                moveRight=False
            if event.key == ord('w'):
                moveUp=False
            if event.key == ord('s'):
                moveDown=False
    print(moveLeft)
    print('textRect '+str(textRect.left))
    if moveLeft and textRect.left > 0:
        print('inside left')
        textRect.move_ip(-1 * PLAYERMOVERATE, 0)
    if moveRight and textRect.right < WINDOWWIDTH:
        textRect.move_ip(PLAYERMOVERATE, 0)
    if moveUp and textRect.top > 0:
        textRect.move_ip(0, -1 * PLAYERMOVERATE)
    if moveDown and textRect.bottom < WINDOWHEIGHT:
        textRect.move_ip(0, PLAYERMOVERATE)
    
    background.fill((44,255,44))
    screen.blit(background, (0, 0))
    screen.blit(text, textRect)
    pygame.display.update()
    #waitForPlayerToPressKey()


