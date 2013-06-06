# https://github.com/RAWKHIGH/
# Name: Stephen McArthur
# Assinment 2
# Slot Machine

import random, pygame, sys
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 480 # size of window's width in pixels
WINDOWHEIGHT = 640 # size of windows' height in pixels

#            R    G    B
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)

strRED = 'Red'
strGREEN = 'Green'
strBLUE = 'Blue'
strORANGE = 'Orange'
strPURPLE = 'Purple'

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Slot Machine Game')

    while True: # main game loop
		
        for event in pygame.event.get():
            if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
        pygame.display.update()
        FPSCLOCK.tick(FPS)
		
	pygame.draw.rect(DISPLAYSURF, WHITE, (  0, 270, 480, 120,))
	pygame.draw.rect(DISPLAYSURF, BLACK, ( 10, 280, 147, 100,))
	pygame.draw.rect(DISPLAYSURF, BLACK, (167, 280, 147, 100,))
	pygame.draw.rect(DISPLAYSURF, BLACK, (324, 280, 147, 100,))
	pygame.draw.rect(DISPLAYSURF, RED,   (  0, 320, 480,   3,))
	
if __name__ == '__main__':
    main()