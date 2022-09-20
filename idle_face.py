#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Sev0r & The_question'

# pip install pygame
import pygame

FPS = 60
width = 800
height = 480

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 225)


pygame.init()
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((800,480))
 
clock = pygame.time.Clock()

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


f = False
g = False
sharp = False
two = False

game_active = True
#exampleimg = pygame.image.load('DSCN8562.JPG')

class Player(object):
	def __init__(self,x,y,image):
		self.x = x
		self.y = y
		self.image = image

    #Method to draw object
	def draw(self):
		#screen.blit(self.image,(self.x,self.y))
		screen.blit(self.image,(self.x,self.y))
    #Method to move object (special input of speedx and speedy)
	def move(self,speedx,speedy):
		self.x += speedx
		self.y += speedy

font = pygame.font.SysFont(None, 48)


window = True
while window:
	clock.tick(FPS)
	
	screen.fill(WHITE)

	pygame.draw.circle(screen, BLUE, (x1, y1), r)
	pygame.draw.circle(screen, RED , (x2, y2), r)
	pygame.draw.rect(screen, GREEN, pygame.Rect(x3, y3, rectwidth, rectheight))
	
	# event = pygame.event.wait()
	# is_pressed = pygame.key.get_pressed()
	f = open("current_value.txt", "r")
	currentValue = f.read().strip();

	font_img = font.render(currentValue, True, BLACK)
	screen.blit(font_img, (width // 2, height // 2))
	
	if currentValue == "exit":
		pygame.quit()
		window = False	
		if not game_active:
			break

	pygame.display.update()
	pygame.display.set_caption("move_circle [{} fps]".format(int(clock.get_fps())))

