# https://github.com/RAWKHIGH/Slot_Machine.git
# Name: Stephen McArthur
# Assinment 2
# Slot Machine

import time, random, pygame
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

pygame.display.set_caption("Stephen'$ Slot Machine")

#Loop until the user clicks the exit button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font=pygame.font.Font(None,30)

# Starting Values  
Player_Money = 1000
Jack_Pot = 500
Bet = 0
message = 'Place Your Bet'

# Background Image
background_image = pygame.image.load("slot-machine.png").convert()

# Exit Button Image
exit_image = pygame.image.load("exit.png").convert()
exit_image.set_colorkey(white)

# Restart Button Image
restart_image = pygame.image.load("restart.png").convert()
restart_image.set_colorkey(white)

# Spin Button Image
spin_image = pygame.image.load("spin.png").convert()
spin_image.set_colorkey(white)

# Preset Bet 100 Image
bet100_image = pygame.image.load("bet100.png").convert()
bet100_image.set_colorkey(white)

# Preset Bet 50 Image
bet50_image = pygame.image.load("bet50.png").convert()
bet50_image.set_colorkey(white)

# Starting Reel 1 Image
reel1_image = pygame.image.load("blank.png").convert()
reel1_image.set_colorkey(white)

# Starting Reel 2 Image
reel2_image = pygame.image.load("blank.png").convert()
reel2_image.set_colorkey(white)

# Starting Reel 3 Image
reel3_image = pygame.image.load("blank.png").convert()
reel3_image.set_colorkey(white)

# Sounds
reel_sound = pygame.mixer.Sound('3_beeps.wav')
coin_sound = pygame.mixer.Sound('coin_drop.wav')
jackpot_sound = pygame.mixer.Sound('Jackpot.wav')

def Reels():
   
    # [0]Fruit, [1]Fruit, [2]Fruit
    Bet_Line = [" "," "," "]
    Outcome = [0,0,0]
    
    # Spin those reels
    for spin in range(3):
        Outcome[spin] = random.randrange(1,65,1)
        # Spin those Reels!
        if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
            Bet_Line[spin] = "Blank"
        if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
            Bet_Line[spin] = "Grapes"
        if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
            Bet_Line[spin] = "Banana"
        if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
            Bet_Line[spin] = "Orange"
        if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
            Bet_Line[spin] = "Cherry"
        if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
            Bet_Line[spin] = "Bar"
        if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
            Bet_Line[spin] = "Bell"  
        if Outcome[spin] == 64:                         # 1.56%  Chance
            Bet_Line[spin] = "Seven"    

    return Bet_Line

# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            done = True			

	# Tracking mouse position and comparing it to where i want buttons
	if event.type == pygame.MOUSEBUTTONDOWN:
		print ('Mouse Clicked')

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
						Player_Money = 1000
						Jack_Pot = 500
						Bet = 0
						message = 'Place Your Bet'
						reel1_image = pygame.image.load("blank.png").convert()
						reel2_image = pygame.image.load("blank.png").convert()
						reel3_image = pygame.image.load("blank.png").convert()
		
		# Bet 100 Button
		elif mouse_x >= bet100_rect.topleft[0] and mouse_y >= bet100_rect.topleft[1]:
			if mouse_x >= bet100_rect.bottomleft[0] and mouse_y <= bet100_rect.bottomleft[1]:
				if mouse_x <= bet100_rect.topright[0] and mouse_y >= bet100_rect.topright[1]:
					if mouse_x <= bet100_rect.bottomright[0] and mouse_y <= bet100_rect.bottomright[1]:
						print ('Betting 100')
						Bet = 100
						coin_sound.play()
						
		# Bet 50 Button
		elif mouse_x >= bet50_rect.topleft[0] and mouse_y >= bet50_rect.topleft[1]:
			if mouse_x >= bet50_rect.bottomleft[0] and mouse_y <= bet50_rect.bottomleft[1]:
				if mouse_x <= bet50_rect.topright[0] and mouse_y >= bet50_rect.topright[1]:
					if mouse_x <= bet50_rect.bottomright[0] and mouse_y <= bet50_rect.bottomright[1]:
						print ('Betting 50')
						Bet = 50
						coin_sound.play()
		
		# Spin Button
		elif mouse_x >= spin_rect.topleft[0] and mouse_y >= spin_rect.topleft[1]:
			if mouse_x >= spin_rect.bottomleft[0] and mouse_y <= spin_rect.bottomleft[1]:
				if mouse_x <= spin_rect.topright[0] and mouse_y >= spin_rect.topright[1]:
					if mouse_x <= spin_rect.bottomright[0] and mouse_y <= spin_rect.bottomright[1]:
						
						# Making sure the Bet does not exceed the current credits 
						if Bet > Player_Money:
							print ('Out of money')
							message = 'Not Enough Credits'
						# Making sure the Bet isn't 0
						elif Bet == 0:
							print ('Did Not Bet')
							message = 'You Did Not Bet'
						# Bet is good
						# Spin Button was clicked
						else:
							print ('Spining')
							reel_sound.play()
							time.sleep(1)
							Jack_Pot += (int(Bet*.5))
							win = False
							Player_Money = Player_Money - Bet
							Fruit_Reel = Reels()
							Fruits = Fruit_Reel[0] + " - " + Fruit_Reel[1] + " - " + Fruit_Reel[2]

							# Match 3
							if Fruit_Reel.count("Grapes") == 3:
								winnings,win = Bet*20,True
							elif Fruit_Reel.count("Banana") == 3:
								winnings,win = Bet*30,True
							elif Fruit_Reel.count("Orange") == 3:
								winnings,win = Bet*40,True
							elif Fruit_Reel.count("Cherry") == 3:
								winnings,win = Bet*100,True
							elif Fruit_Reel.count("Bar") == 3:
								winnings,win = Bet*200,True
							elif Fruit_Reel.count("Bell") == 3:
								winnings,win = Bet*300,True
							elif Fruit_Reel.count("Seven") == 3:
								print("Lucky Seven!!!")
								winnings,win = Bet*1000,True
							# Match 2
							elif Fruit_Reel.count("Blank") == 0:
								if Fruit_Reel.count("Grapes") == 2:
									winnings,win = Bet*2,True
								if Fruit_Reel.count("Banana") == 2:
									winnings,win = Bet*2,True
								elif Fruit_Reel.count("Orange") == 2:
									winnings,win = Bet*3,True
								elif Fruit_Reel.count("Cherry") == 2:
									winnings,win = Bet*4,True
								elif Fruit_Reel.count("Bar") == 2:
									winnings,win = Bet*5,True
								elif Fruit_Reel.count("Bell") == 2:
									winnings,win = Bet*10,True
								elif Fruit_Reel.count("Seven") == 2:
									winnings,win = Bet*20,True
								
								# Match Lucky Seven
								elif Fruit_Reel.count("Seven") == 1:
									winnings, win = Bet*10,True
								else:
									winnings, win = Bet*2,True
							if win:
								message = "You Won " + str(int(winnings)) + ' Credits'
								print(Fruits + "\n" + "You Won $ " + str(int(winnings)) + " !!! \n")
								Player_Money += int(winnings)
		
								# Jackpot 1 in 450 chance of winning
								jackpot_try = random.randrange(1,51,1)
								jackpot_win = random.randrange(1,51,1)
								if  jackpot_try  == jackpot_win:
									message = "You Won The Jackpot $" + str(Jack_Pot)
									jackpot_sound.play()
									print ("You Won The Jackpot !!!\nHere is your $ " + str(Jack_Pot) + "prize! \n")
									Jack_Pot = 500
								elif jackpot_try != jackpot_win:
									print ("You did not win the Jackpot this time. \nPlease try again ! \n")
								# No win
								else:
									print(Fruits + "\nPlease try again. \n")
							else:
								message = 'Not a Winner'
							
							if Fruit_Reel[0] == "Grapes":
								reel1_image = pygame.image.load("Sic_Emoticon.png").convert()
							elif Fruit_Reel[0] == "Banana":
								reel1_image = pygame.image.load("Sad_Emoticon.png").convert()
							elif Fruit_Reel[0] == "Orange":
								reel1_image = pygame.image.load("Raspberry_Emoticon.png").convert()
							elif Fruit_Reel[0] == "Cherry":
								reel1_image = pygame.image.load("Mad_Emoticon.png").convert()
							elif Fruit_Reel[0] == "Bar":
								reel1_image = pygame.image.load("Laugh_Emoticon.png").convert()
							elif Fruit_Reel[0] == "Bell":
								reel1_image = pygame.image.load("Happy_Emoticon.png").convert()
							elif Fruit_Reel[0] == "Seven":
								reel1_image = pygame.image.load("Surprised_Emoticon.png").convert()
							else:
								reel1_image = pygame.image.load("blank.png").convert()
														
							if Fruit_Reel[1] == "Grapes":
								reel2_image = pygame.image.load("Sic_Emoticon.png").convert()
							elif Fruit_Reel[1] == "Banana":
								reel2_image = pygame.image.load("Sad_Emoticon.png").convert()
							elif Fruit_Reel[1] == "Orange":
								reel2_image = pygame.image.load("Raspberry_Emoticon.png").convert()
							elif Fruit_Reel[1] == "Cherry":
								reel2_image = pygame.image.load("Mad_Emoticon.png").convert()
							elif Fruit_Reel[1] == "Bar":
								reel2_image = pygame.image.load("Laugh_Emoticon.png").convert()
							elif Fruit_Reel[1] == "Bell":
								reel2_image = pygame.image.load("Happy_Emoticon.png").convert()
							elif Fruit_Reel[1] == "Seven":
								reel2_image = pygame.image.load("Surprised_Emoticon.png").convert()
							else:
								reel2_image = pygame.image.load("blank.png").convert()
								
							if Fruit_Reel[2] == "Grapes":
								reel3_image = pygame.image.load("Sic_Emoticon.png").convert()
							elif Fruit_Reel[2] == "Banana":
								reel3_image = pygame.image.load("Sad_Emoticon.png").convert()
							elif Fruit_Reel[2] == "Orange":
								reel3_image = pygame.image.load("Raspberry_Emoticon.png").convert()
							elif Fruit_Reel[2] == "Cherry":
								reel3_image = pygame.image.load("Mad_Emoticon.png").convert()
							elif Fruit_Reel[2] == "Bar":
								reel3_image = pygame.image.load("Laugh_Emoticon.png").convert()
							elif Fruit_Reel[2] == "Bell":
								reel3_image = pygame.image.load("Happy_Emoticon.png").convert()
							elif Fruit_Reel[2] == "Seven":
								reel3_image = pygame.image.load("Surprised_Emoticon.png").convert()
							else:
								reel3_image = pygame.image.load("blank.png").convert()
	
	# Putting Background Image On Screen
	screen.blit(background_image, [0,0])
	
	# Putting Exit Image on screen and a rectangle to compare for button
	exit_rect = pygame.draw.rect(screen, black,(314,538, 50, 25,))
	screen.blit(exit_image, [314,538])

	# Putting Restart Image on screen and a rectangle to compare for button
	restart_rect = pygame.draw.rect(screen, black,(520,420, 75, 24,))
	screen.blit(restart_image, [520,420])

	# Putting Spin Image on screen and a rectangle to compare for button
	spin_rect = pygame.draw.rect(screen, black,(505,155,106,105,))
	screen.blit(spin_image, [505,155])

	# Putting Bet 100 Image on screen and a rectangle to compare for button
	bet100_rect = pygame.draw.rect(screen, black,(562,366, 53, 52,))
	screen.blit(bet100_image, [562,366])

	# Putting Bet 50 Image on screen and a rectangle to compare for button
	bet50_rect = pygame.draw.rect(screen, black,(505,366, 53, 52,))
	screen.blit(bet50_image, [505,366])
	
	# Putting Reel Images on screen
	screen.blit(reel1_image, [120,250])
	screen.blit(reel2_image, [250,250])
	screen.blit(reel3_image, [380,250])

	# Deturmaning mouse position for button use and print statement for 
	# when trying to aline everything
	mouse_position = pygame.mouse.get_pos()
	mouse_x = mouse_position[0]
	mouse_y = mouse_position[1]
	#print (mouse_position)
	
	# assigning text to veriables
	jackpotText = font.render("JackPot: "+str(Jack_Pot), 1, white)
	player_moneyText = font.render(str(Player_Money), 1, black)
	betText = font.render(str(Bet), 1, black)
	messageText = font.render(str(message), 1, white)

	# Place text on screen
	screen.blit(jackpotText, (245, 125))
	screen.blit(player_moneyText, (539, 71))
	screen.blit(betText, (555, 300))
	screen.blit(messageText, (200, 493))
	
    pygame.display.flip()
 
    clock.tick(30) # Limit to 30 frames per second

pygame.quit()