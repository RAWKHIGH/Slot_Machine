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

exit_image = pygame.image.load("exit.png").convert()
exit_image.set_colorkey(white)


# -------- Main Program Loop -----------
while done == False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True			# Flag that we are done so we exit this loop
			
			
	if event.type == pygame.MOUSEBUTTONDOWN:
		print ('Mouse CLicked')
		if mouse_x >= exit_rect.topleft[0] and mouse_y >= exit_rect.topleft[1]:
			print ('Top left')
			if mouse_x >= exit_rect.bottomleft[0] and mouse_y <= exit_rect.bottomleft[1]:
				print ('bottom left')
				if mouse_x <= exit_rect.topright[0] and mouse_y >= exit_rect.topright[1]:
					print ('Top right')
					if mouse_x <= exit_rect.bottomright[0] and mouse_y <= exit_rect.bottomright[1]:
						print ('Bottom Right')
						done = True
						
						
						
						
	screen.blit(background_image, [0,0])
	exit_rect = pygame.draw.rect(screen, black,   (  314, 538, 50,   25,))	
	screen.blit(exit_image, [314,538])
		
	mouse_position = pygame.mouse.get_pos()
	mouse_x = mouse_position[0]
	mouse_y = mouse_position[1]
	print (mouse_position)

	
    pygame.display.flip()
 
    clock.tick(20) # Limit to 20 frames per second

pygame.quit()
