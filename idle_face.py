#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Sev0r & The_question'

# pip install pygame
import pygame
import py

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



window = True
while window:
	for event in pygame.event.get():
		
		screen.fill(WHITE)

		pygame.draw.circle(screen, BLUE, (x1, y1), r)
		pygame.draw.circle(screen, RED , (x2, y2), r)
		pygame.draw.rect(screen, GREEN, pygame.Rect(x3, y3, rectwidth, rectheight))	
		
		event = pygame.event.wait()
		is_pressed = pygame.key.get_pressed()
		
		if is_pressed[pygame.K_ESCAPE]:
			pygame.quit()
			window = False	
			if not game_active:
				break				
					
		if is_pressed[pygame.K_0]:
			if is_pressed[pygame.K_c]:
				print("C0")
				#player = Player(100,100,exampleimg)
				#player.draw()
				#screen.blit(exampleimg,(100,100))
				#pygame.display.update()
			elif is_pressed[pygame.K_k]:
				print("C#0")
			elif is_pressed[pygame.K_d]:
				print("D0")
			elif is_pressed[pygame.K_b]:
				print("D#0")
			elif is_pressed[pygame.K_e]:
				print("E0")
			elif is_pressed[pygame.K_f]:
				print("F0")
			elif is_pressed[pygame.K_v]:
				print("F#0")
			elif is_pressed[pygame.K_g]:
				print("G0")
			elif is_pressed[pygame.K_p]:
				print("G#0")
			elif is_pressed[pygame.K_a]:
				print("A0")
			elif is_pressed[pygame.K_o]:
				print("A#0")
			elif is_pressed[pygame.K_h]:
				print("H0")
		elif is_pressed[pygame.K_1]:
			if is_pressed[pygame.K_c]:
				print("C1")
			elif is_pressed[pygame.K_k]:
				print("C#1")
			elif is_pressed[pygame.K_d]:
				print("D1")
			elif is_pressed[pygame.K_b]:
				print("D#1")
			elif is_pressed[pygame.K_e]:
				print("E1")
			elif is_pressed[pygame.K_f]:
				print("F1")
			elif is_pressed[pygame.K_v]:
				print("F#1")
			elif is_pressed[pygame.K_g]:
				print("G1")
			elif is_pressed[pygame.K_p]:
				print("G#1")
			elif is_pressed[pygame.K_a]:
				print("A1")
			elif is_pressed[pygame.K_o]:
				print("A#1")
			elif is_pressed[pygame.K_h]:
				print("H1")
		elif is_pressed[pygame.K_2]:
			if is_pressed[pygame.K_c]:
				print("C2")
			elif is_pressed[pygame.K_k]:
				print("C#2")
			elif is_pressed[pygame.K_d]:
				print("D2")
			elif is_pressed[pygame.K_b]:
				print("D#2")
			elif is_pressed[pygame.K_e]:
				print("E2")
			elif is_pressed[pygame.K_f]:
				print("F2")
			elif is_pressed[pygame.K_v]:
				print("F#2")
			elif is_pressed[pygame.K_g]:
				print("G2")
			elif is_pressed[pygame.K_p]:
				print("G#2")
			elif is_pressed[pygame.K_a]:
				print("A2")
			elif is_pressed[pygame.K_o]:
				print("A#2")
			elif is_pressed[pygame.K_h]:
				print("H2")
		elif is_pressed[pygame.K_3]:
			if is_pressed[pygame.K_c]:
				print("C3")
			elif is_pressed[pygame.K_k]:
				print("C#3")
			elif is_pressed[pygame.K_d]:
				print("D3")
			elif is_pressed[pygame.K_b]:
				print("D#3")
			elif is_pressed[pygame.K_e]:
				print("E3")
			elif is_pressed[pygame.K_f]:
				print("F3")
			elif is_pressed[pygame.K_v]:
				print("F#3")
			elif is_pressed[pygame.K_g]:
				print("G3")
			elif is_pressed[pygame.K_p]:
				print("G#3")
			elif is_pressed[pygame.K_a]:
				print("A3")
			elif is_pressed[pygame.K_o]:
				print("A#3")
			elif is_pressed[pygame.K_h]:
				print("H3")
		elif is_pressed[pygame.K_4]:
			if is_pressed[pygame.K_c]:
				print("C4")
			elif is_pressed[pygame.K_k]:
				print("C#4")
			elif is_pressed[pygame.K_d]:
				print("D4")
			elif is_pressed[pygame.K_b]:
				print("D#4")
			elif is_pressed[pygame.K_e]:
				print("E4")
			elif is_pressed[pygame.K_f]:
				print("F4")
			elif is_pressed[pygame.K_v]:
				print("F#4")
			elif is_pressed[pygame.K_g]:
				print("G4")
			elif is_pressed[pygame.K_p]:
				print("G#4")
			elif is_pressed[pygame.K_a]:
				print("A4")
			elif is_pressed[pygame.K_o]:
				print("A#4")
			elif is_pressed[pygame.K_h]:
				print("H4")
		elif is_pressed[pygame.K_5]:
			if is_pressed[pygame.K_c]:
				print("C5")
			elif is_pressed[pygame.K_k]:
				print("C#5")
			elif is_pressed[pygame.K_d]:
				print("D5")
			elif is_pressed[pygame.K_b]:
				print("D#5")
			elif is_pressed[pygame.K_e]:
				print("E5")
			elif is_pressed[pygame.K_f]:
				print("F5")
			elif is_pressed[pygame.K_v]:
				print("F#5")
			elif is_pressed[pygame.K_g]:
				print("G5")
			elif is_pressed[pygame.K_p]:
				print("G#5")
			elif is_pressed[pygame.K_a]:
				print("A5")
			elif is_pressed[pygame.K_o]:
				print("A#5")
			elif is_pressed[pygame.K_h]:
				print("H5")
		elif is_pressed[pygame.K_6]:
			if is_pressed[pygame.K_c]:
				print("C6")
			elif is_pressed[pygame.K_k]:
				print("C#6")
			elif is_pressed[pygame.K_d]:
				print("D6")
			elif is_pressed[pygame.K_b]:
				print("D#6")
			elif is_pressed[pygame.K_e]:
				print("E6")
			elif is_pressed[pygame.K_f]:
				print("F6")
			elif is_pressed[pygame.K_v]:
				print("F#6")
			elif is_pressed[pygame.K_g]:
				print("G6")
			elif is_pressed[pygame.K_p]:
				print("G#6")
			elif is_pressed[pygame.K_a]:
				print("A6")
			elif is_pressed[pygame.K_o]:
				print("A#6")
			elif is_pressed[pygame.K_h]:
				print("H6")
		elif is_pressed[pygame.K_7]:
			if is_pressed[pygame.K_c]:
				print("C7")
			elif is_pressed[pygame.K_k]:
				print("C#7")
			elif is_pressed[pygame.K_d]:
				print("D7")
			elif is_pressed[pygame.K_b]:
				print("D#7")
			elif is_pressed[pygame.K_e]:
				print("E7")
			elif is_pressed[pygame.K_f]:
				print("F7")
			elif is_pressed[pygame.K_v]:
				print("F#7")
			elif is_pressed[pygame.K_g]:
				print("G7")
			elif is_pressed[pygame.K_p]:
				print("G#7")
			elif is_pressed[pygame.K_a]:
				print("A7")
			elif is_pressed[pygame.K_o]:
				print("A#7")
			elif is_pressed[pygame.K_h]:
				print("H7")
		elif is_pressed[pygame.K_8]:
			if is_pressed[pygame.K_c]:
				print("C8")
			elif is_pressed[pygame.K_k]:
				print("C#8")
			elif is_pressed[pygame.K_d]:
				print("D8")
			elif is_pressed[pygame.K_b]:
				print("D#8")
			elif is_pressed[pygame.K_e]:
				print("E8")
			elif is_pressed[pygame.K_f]:
				print("F8")
			elif is_pressed[pygame.K_v]:
				print("F#8")
			elif is_pressed[pygame.K_g]:
				print("G8")
			elif is_pressed[pygame.K_p]:
				print("G#8")
			elif is_pressed[pygame.K_a]:
				print("A8")
			elif is_pressed[pygame.K_o]:
				print("A#8")
			elif is_pressed[pygame.K_h]:
				print("H8")
		elif is_pressed[pygame.K_9]:
			if is_pressed[pygame.K_c]:
				print("C9")
			elif is_pressed[pygame.K_k]:
				print("C#9")
			elif is_pressed[pygame.K_d]:
				print("D9")
			elif is_pressed[pygame.K_b]:
				print("D#9")
			elif is_pressed[pygame.K_e]:
				print("E9")
			elif is_pressed[pygame.K_f]:
				print("F9")
			elif is_pressed[pygame.K_v]:
				print("F#9")
			elif is_pressed[pygame.K_g]:
				print("G9")
			elif is_pressed[pygame.K_p]:
				print("G#9")
			elif is_pressed[pygame.K_a]:
				print("A9")
			elif is_pressed[pygame.K_o]:
				print("A#9")
			elif is_pressed[pygame.K_h]:
				print("H9")


		pygame.display.update()
		pygame.display.set_caption("move_circle [{} fps]".format(int(clock.get_fps())))

		clock.tick(FPS)
