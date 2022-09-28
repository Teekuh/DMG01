#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Sev0r & The_question & AliasRoot'


import pygame.display
import pygame.font
import pygame.time
import pygame.draw
import pygame.event
import pygame.surface


FPS = 60
width = 800
height = 480

#--- Test Colors -------------------------------------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.display.init()
pygame.font.init()

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((800,480))


#--- Load images -------------------------------------------------------
idle_001 = pygame.image.load('img/IDLE/IDLE_001.png')
idle_002 = pygame.image.load('img/IDLE/IDLE_002.png')
idle_003 = pygame.image.load('img/IDLE/IDLE_003.png')
idle_004 = pygame.image.load('img/IDLE/IDLE_004.png')
idle_005 = pygame.image.load('img/IDLE/IDLE_005.png')
idle_006 = pygame.image.load('img/IDLE/IDLE_006.png')
idle_007 = pygame.image.load('img/IDLE/IDLE_007.png')
idle_008 = pygame.image.load('img/IDLE/IDLE_008.png')
#-----------------------------------------------------------------------
wink_001 = pygame.image.load('img/WINK/WINK_001.png')
wink_002 = pygame.image.load('img/WINK/WINK_002.png')



#--- Initialise Idle-Animation -----------------------------------------
bpm = 120;
step = (60000 // bpm ) // 4
sequence = ["idle"];

#--- Clear current_value.txt -------------------------------------------
currentValue = ""
note = open("current_value.txt", "w")
note.truncate()

#font = pygame.font.SysFont(None,48)

done = False
clock = pygame.time.Clock()

#--- Length of bar in ms -----------------------------------------------
def getLengthOfBar(bpm):
	step = (60000 // bpm ) // 4
	return step


#--- Animation-Loops ---------------------------------------------------
def animate(animation, frame):
	if(animation == "idle"):
		if(frame == 0):
			screen.blit(idle_001,(0,0))
		if(frame == 1):
			screen.blit(idle_001,(0,0))
		if(frame == 2):
			screen.blit(idle_002,(0,0))
		if(frame == 3):
			screen.blit(idle_002,(0,0))
		if(frame == 4):
			screen.blit(idle_003,(0,0))
		if(frame == 5):
			screen.blit(idle_003,(0,0))
		if(frame == 6):
			screen.blit(idle_004,(0,0))
		if(frame == 7):
			screen.blit(idle_004,(0,0))
		if(frame == 8):
			screen.blit(idle_005,(0,0))
		if(frame == 9):
			screen.blit(idle_005,(0,0))
		if(frame == 10):
			screen.blit(idle_006,(0,0))
		if(frame == 11):
			screen.blit(idle_006,(0,0))
		if(frame == 12):
			screen.blit(idle_007,(0,0))
		if(frame == 13):
			screen.blit(idle_007,(0,0))
		if(frame == 14):
			screen.blit(idle_008,(0,0))
		if(frame == 15):
			screen.blit(idle_008,(0,0))
#-----------------------------------------------------------------------
	if(animation == "wink"):
		if(frame == 0):
			screen.blit(wink_001,(0,0))
		if(frame == 1):
			screen.blit(wink_001,(0,0))
		if(frame == 2):
			screen.blit(wink_001,(0,0))
		if(frame == 3):
			screen.blit(wink_001,(0,0))
		if(frame == 4):
			screen.blit(wink_001,(0,0))
		if(frame == 5):
			screen.blit(wink_001,(0,0))
		if(frame == 6):
			screen.blit(wink_001,(0,0))
		if(frame == 7):
			screen.blit(wink_002,(0,0))
		if(frame == 8):
			screen.blit(wink_002,(0,0))
		if(frame == 9):
			screen.blit(wink_002,(0,0))
		if(frame == 10):
			screen.blit(wink_002,(0,0))
		if(frame == 11):
			screen.blit(wink_002,(0,0))
		if(frame == 12):
			screen.blit(wink_002,(0,0))
		if(frame == 13):
			screen.blit(wink_002,(0,0))
		if(frame == 14):
			screen.blit(wink_002,(0,0))
		if(frame == 15):
			screen.blit(wink_002,(0,0))
#-----------------------------------------------------------------------


currentAnimationIndex = 0;
currentAnimationFrame = 0;
startTimeCurrentChain = pygame.time.get_ticks()

#--- Main --------------------------------------------------------------
while not done:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill(WHITE)
	
	#------ Listen for Input -------------------------------------------
	note = open("current_value.txt", "r")
	lastValue = currentValue;
	currentValue = note.read().strip();
	#-------------------------------------------------------------------
	
	if(currentValue != lastValue):
		if(currentValue == "41"):
			#Test-Song 1
			sequence = ["idle","wink","idle","wink","idle","wink","idle","wink"];
			currentAnimationIndex = 0;
			currentAnimationFrame = 0;
			time = 44;
			bpm = 240;
			startTimeCurrentChain = pygame.time.get_ticks()
			note = open("current_value.txt", "w")
			note.truncate()
			
		if(currentValue == "42"):
			#Test-Song 2
			sequence = ["idle","idle","idle","idle","idle","idle","idle","idle"];
			currentAnimationIndex = 0;
			currentAnimationFrame = 0;
			time = 44;
			bpm = 240;
			startTimeCurrentChain = pygame.time.get_ticks()
			note = open("current_value.txt", "w")
			note.truncate()
	
	
	#to do: Button to reset to idle, sequence = ["idle"] & bpm = 120
	currentAnimation = sequence[currentAnimationIndex];
	
	animate(currentAnimation, currentAnimationFrame)
	
	#to-do: Only update after correct ms based on bpm
	
	timePassed = pygame.time.get_ticks() - startTimeCurrentChain 
	currentAnimationFrame = timePassed // getLengthOfBar(bpm)
	
	if(currentAnimationFrame > 15):
		currentAnimationFrame = 0
		currentAnimationIndex += 1
		startTimeCurrentChain = pygame.time.get_ticks()
	if(currentAnimationIndex >= len(sequence)):
		sequence = ["idle"]
		currentAnimationIndex = 0
		bpm = 120
	
	#font_img = font.render(currentValue, True, BLACK)
	#screen.blit(font_img, (width // 2, height // 2))
				
	
	clock.tick(FPS)

	pygame.display.flip()
	pygame.display.set_caption("move_circle [{} fps]".format(int(clock.get_fps()))) 
			
