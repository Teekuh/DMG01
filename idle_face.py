#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Sev0r & The_question'

# pip install pygame
import pygame

FPS = 60
width = 800
height = 480

#Test Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 225)


pygame.init()
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((800,480))






x1 = width // 3
x2 = width - x1
y1 = height // 3
y2 = height // 3
r = 50
x3 = width // 4
y3 = 3*height // 4
rectwidth  = 400
rectheight = 100
step = 50


font = pygame.font.SysFont(None,48)

done = False
clock = pygame.time.Clock()


#------Main---------------------------------------------------------------------
while not done:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill(WHITE)

	pygame.draw.circle(screen, BLUE, (x1, y1), r)
	pygame.draw.circle(screen, RED , (x2, y2), r)
	pygame.draw.rect(screen, GREEN, pygame.Rect(x3, y3, rectwidth, rectheight))
	
	f = open("current_value.txt", "r")
	currentValue = f.read().strip();
	
	font_img = font.render(currentValue, True, BLACK)
	screen.blit(font_img, (width // 2, height // 2))
				
			
	if(currentValue == "41"):
		#F2
		pygame.draw.circle(screen, BLUE, (x1, y1), r)
		pygame.draw.circle(screen, BLUE , (x2, y2), r)
		pygame.draw.rect(screen, BLUE, pygame.Rect(x3, y3, rectwidth, rectheight))
		font_img = font.render('F2', True, BLACK)
		screen.blit(font_img, (width // 2, height // 2 + 40))
		
	elif(currentValue == "42"):
		#F#2
		pygame.draw.circle(screen, RED, (x1, y1), r)
		pygame.draw.circle(screen, RED , (x2, y2), r)
		pygame.draw.rect(screen, RED, pygame.Rect(x3, y3, rectwidth, rectheight))
		font_img = font.render('F#2', True, BLACK)
		screen.blit(font_img, (width // 2, height // 2 + 40))
	
	clock.tick(FPS)

	pygame.display.flip()
	pygame.display.set_caption("move_circle [{} fps]".format(int(clock.get_fps()))) 
			
