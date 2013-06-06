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

restart_image = pygame.image.load("restart.png").convert()
restart_image.set_colorkey(white)

spin_image = pygame.image.load("spin.png").convert()
spin_image.set_colorkey(white)

# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            done = True			# Flag that we are done so we exit this loop
	
	# Tracking mouse position and comparing it to where i want buttons
	if event.type == pygame.MOUSEBUTTONDOWN:
		print ('Mouse CLicked')
		
		# Exit Button
		if mouse_x >= exit_rect.topleft[0] and mouse_y >= exit_rect.topleft[1]:
			if mouse_x >= exit_rect.bottomleft[0] and mouse_y <= exit_rect.bottomleft[1]:
				if mouse_x <= exit_rect.topright[0] and mouse_y >= exit_rect.topright[1]:
					if mouse_x <= exit_rect.bottomright[0] and mouse_y <= exit_rect.bottomright[1]:
						print ('Game Exited')
						done = True
		
		# Reset Button
		elif mouse_x >= restart_rect.topleft[0] and mouse_y >= restart_rect.topleft[1]:
			print ('Restart Top Left')
			if mouse_x >= restart_rect.bottomleft[0] and mouse_y <= restart_rect.bottomleft[1]:
				print ('Restart Bottom Left')
				if mouse_x <= restart_rect.topright[0] and mouse_y >= restart_rect.topright[1]:
					print ('Restart Top Right')
					if mouse_x <= restart_rect.bottomright[0] and mouse_y <= restart_rect.bottomright[1]:
						print ('Restart Bottom Right')
						print ('App Resetted')
		
		# Spin Button
		elif mouse_x >= spin_rect.topleft[0] and mouse_y >= spin_rect.topleft[1]:
			print ('Spin Top Left')
			if mouse_x >= spin_rect.bottomleft[0] and mouse_y <= spin_rect.bottomleft[1]:
				print ('Spin Bottom Left')
				if mouse_x <= spin_rect.topright[0] and mouse_y >= spin_rect.topright[1]:
					print ('Spin Top Right')
					if mouse_x <= spin_rect.bottomright[0] and mouse_y <= spin_rect.bottomright[1]:
						print ('Spin Bottom Right')
	
	
	
	
	
	screen.blit(background_image, [0,0])
	
	exit_rect = pygame.draw.rect(screen, black,(314,538, 50, 25,))
	screen.blit(exit_image, [314,538])
	
	restart_rect = pygame.draw.rect(screen, black,(520,420, 75, 24,))
	screen.blit(restart_image, [520,420])
	
	spin_rect = pygame.draw.rect(screen, black,(505,155,106,105,))
	screen.blit(spin_image, [505,155])
	
	mouse_position = pygame.mouse.get_pos()
	mouse_x = mouse_position[0]
	mouse_y = mouse_position[1]
	print (mouse_position)

	
    pygame.display.flip()
 
    clock.tick(30) # Limit to 30 frames per second

pygame.quit()
