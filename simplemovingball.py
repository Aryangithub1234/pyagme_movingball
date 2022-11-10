import pygame
from pygame.locals import *    #colors ko dictionary ki form meh rkhne k liye
size = 800 , 400   #screen size
width , height = size   #chaudayi aur lambai
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

pygame.init()  #initialisation
screen = pygame.display.set_mode(size)   #set display

mydict = { K_b : BLACK , K_r:RED , K_g:GREEN , K_b:BLUE , K_y:YELLOW,
    K_c:CYAN , K_m:MAGENTA  }
# print(mydict)
running = True
ball = pygame.image.load('ball.gif')  #game meh kisi b image ko load krne k liye
rect = ball.get_rect()
speed = [1,1]
backgrd = BLACK
while True:
    for event in pygame.event.get():  #important event loops
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in mydict:
                backgrd = mydict[event.key]
                caption = " Aryan_gaming(window) "
                pygame.display.set_caption(caption)
    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(backgrd)
    pygame.draw.rect(screen,RED,rect,1)
    screen.blit(ball,rect)
    pygame.display.update()
pygame.quit()