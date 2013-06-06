# https://github.com/RAWKHIGH/
# Name: Stephen McArthur
# Assinment 2
# Slot Machine
  
import pygame
from pygame.locals import *
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
 
pygame.init()
  
# Set the width and height of the screen [width,height]
size = [651,588]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Slot Machine")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

background_image = pygame.image.load("slot-machine.png").convert()  
# -------- Main Program Loop -----------
while done == False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True			# Flag that we are done so we exit this loop
			
	if event.type == pygame.MOUSEBUTTONDOWN:
		print ('mouse clicked')
			
			
			
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
  
  
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
     
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
     
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.blit(background_image, [0,0])
    

	
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
     
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(20)    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
