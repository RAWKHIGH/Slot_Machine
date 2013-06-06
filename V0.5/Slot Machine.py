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

font=pygame.font.Font(None,30)

Player_Money = 1000
Jack_Pot = 500
Bet = 0
message = 'Place Your Bet'

background_image = pygame.image.load("slot-machine.png").convert()

exit_image = pygame.image.load("exit.png").convert()
exit_image.set_colorkey(white)

restart_image = pygame.image.load("restart.png").convert()
restart_image.set_colorkey(white)

spin_image = pygame.image.load("spin.png").convert()
spin_image.set_colorkey(white)

bet100_image = pygame.image.load("bet100.png").convert()
bet100_image.set_colorkey(white)

bet50_image = pygame.image.load("bet50.png").convert()
bet50_image.set_colorkey(white)

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
			if mouse_x >= restart_rect.bottomleft[0] and mouse_y <= restart_rect.bottomleft[1]:
				if mouse_x <= restart_rect.topright[0] and mouse_y >= restart_rect.topright[1]:
					if mouse_x <= restart_rect.bottomright[0] and mouse_y <= restart_rect.bottomright[1]:
						print ('Game Restart')
		
		# Bet 100 Button
		elif mouse_x >= bet100_rect.topleft[0] and mouse_y >= bet100_rect.topleft[1]:
			if mouse_x >= bet100_rect.bottomleft[0] and mouse_y <= bet100_rect.bottomleft[1]:
				if mouse_x <= bet100_rect.topright[0] and mouse_y >= bet100_rect.topright[1]:
					if mouse_x <= bet100_rect.bottomright[0] and mouse_y <= bet100_rect.bottomright[1]:
						print ('Beting 100')
						Bet = 100
						Player_Money = Player_Money - Bet
						
		# Bet 50 Button
		elif mouse_x >= bet50_rect.topleft[0] and mouse_y >= bet50_rect.topleft[1]:
			if mouse_x >= bet50_rect.bottomleft[0] and mouse_y <= bet50_rect.bottomleft[1]:
				if mouse_x <= bet50_rect.topright[0] and mouse_y >= bet50_rect.topright[1]:
					if mouse_x <= bet50_rect.bottomright[0] and mouse_y <= bet50_rect.bottomright[1]:
						print ('Beting 50')
						Bet = 50
						Player_Money = Player_Money - Bet
		
		# Spin Button
		elif mouse_x >= spin_rect.topleft[0] and mouse_y >= spin_rect.topleft[1]:
			if mouse_x >= spin_rect.bottomleft[0] and mouse_y <= spin_rect.bottomleft[1]:
				if mouse_x <= spin_rect.topright[0] and mouse_y >= spin_rect.topright[1]:
					if mouse_x <= spin_rect.bottomright[0] and mouse_y <= spin_rect.bottomright[1]:
						print ('Spining')
						
	screen.blit(background_image, [0,0])

	exit_rect = pygame.draw.rect(screen, black,(314,538, 50, 25,))
	screen.blit(exit_image, [314,538])

	restart_rect = pygame.draw.rect(screen, black,(520,420, 75, 24,))
	screen.blit(restart_image, [520,420])

	spin_rect = pygame.draw.rect(screen, black,(505,155,106,105,))
	screen.blit(spin_image, [505,155])

	bet100_rect = pygame.draw.rect(screen, black,(562,366, 53, 52,))
	screen.blit(bet100_image, [562,366])

	bet50_rect = pygame.draw.rect(screen, black,(505,366, 53, 52,))
	screen.blit(bet50_image, [505,366])

	mouse_position = pygame.mouse.get_pos()
	mouse_x = mouse_position[0]
	mouse_y = mouse_position[1]
	print (mouse_position)
	
	jackpotText = font.render("JackPot: "+str(Jack_Pot), 1, white)
	player_moneyText = font.render(str(Player_Money), 1, black)
	betText = font.render(str(Bet), 1, black)
	messageText = font.render(str(message), 1, white)

	screen.blit(jackpotText, (245, 125))
	screen.blit(player_moneyText, (539, 71))
	screen.blit(betText, (555, 300))
	screen.blit(messageText, (265, 493))

	pygame.display.flip()

	clock.tick(20)

pygame.quit()