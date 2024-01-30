import pygame
import math
import time 
import random 
pygame.font.init

# انا بجهز النافدة 
w,h = 600 , 600 
win = pygame.display.set_mode((w,h))

pygame.display.set_caption("space war")
backgraound = pygame.image.load ("bg.jpeg")


def draw ():
    win.blit(backgraound , (0,0))

pygame.display.update()

def main ():

    run = True
    while run :
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

pygame.quit()


if __name__ == "__main__":
    main()