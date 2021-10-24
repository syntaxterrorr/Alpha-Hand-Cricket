import pygame,logic,hand_cricket_main
import os,sys
from collections import Counter
import popen
from pygame.locals import *


# def main():
# 	pygame.init()
# 	screen = pygame.display.set_mode((1920, 1080))
#
# 	clock = pygame.time.Clock()
#
# 	while 1:
# 		mouse = pygame.mouse.get_pos()
# 		click = pygame.mouse.get_pressed()
# 		screen.fill((255, 255, 0))
# 		font = pygame.font.SysFont("comicsansms", 72)
# 		button_font = pygame.font.SysFont("comicsansms", 30)
# 		text = font.render("Alpha Hand-Cricket", True, (0, 128, 0))
#
# 		re_button_text = button_font.render("Replay", True, (0, 0, 0))
# 		ex_button_text = button_font.render("Exit", True, (0, 0, 0))
#
# 		# image = cam.get_image()
# 		pygame.draw.rect(screen, (0, 255, 0),(1550,20,100,50))
# 		screen.blit(re_button_text,(1565,35))
# 		pygame.draw.rect(screen, (255, 0, 0),(1700,20,100,50))
# 		screen.blit(ex_button_text,(1730,35))
# 		screen.blit(text,(760,35))
#
# 		# screen.blit(image, (1200,520))
# 		pygame.display.update()
#
# 		if(click[0]==1):
# 			print("close")
# 			if(1800>mouse[0]>1700 and 70>mouse[1]>20):
# 				sys.exit()
#
# 		if(click[0]==1):
# 			if(1650>mouse[0]>1550 and 70>mouse[1]>20):
# 				logic.main()
# 		#
# 		# for event in pygame.event.get():
# 		# 	if event.type == pygame.QUIT:
# 		# 		sys.exit()

def user_move():
	o=popen.output()
	number=Counter(o)
	s = max(number.values())
	i = number.values().index(s)
	move=int(number.items()[i][0])
	return move


def confirm():
	pygame.init()
	screen = pygame.display.set_mode((1920, 1080))

	clock = pygame.time.Clock()

	def pic(o):
		if(o==1):
			return pygame.image.load("/home/kushald/Downloads/one.jpg")
		elif(o==2):
			return pygame.image.load("/home/kushald/Downloads/two.jpg")
		elif(o==3):
			return pygame.image.load("/home/kushald/Downloads/three.jpg")
		elif(o==4):
			return pygame.image.load("/home/kushald/Downloads/four.jpg")
		elif(o==5):
			return pygame.image.load("/home/kushald/Downloads/five.jpg")
		elif(o==6):
			return pygame.image.load("/home/kushald/Downloads/six.jpg")
		else:
			return pygame.image.load("/home/kushald/Downloads/screen-2.jpg")

	play=True


	while play:
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		screen.fill((255, 255, 0))
		font = pygame.font.SysFont("comicsansms", 72)
		button_font = pygame.font.SysFont("comicsansms", 30)
		text = font.render("Click on PLAY to begin the game", True, (0, 128, 0))

		re_button_text = button_font.render("PLAY", True, (0, 0, 0))
		ex_button_text = button_font.render("EXIT", True, (0, 0, 0))

		# image = cam.get_image()
		pygame.draw.rect(screen, (0, 255, 0),(1550,20,100,50))
		screen.blit(re_button_text,(1570,35))
		pygame.draw.rect(screen, (255, 0, 0),(1700,20,100,50))
		screen.blit(ex_button_text,(1725,35))
		screen.blit(text,(760,735))

		# o=popen.output()
		# number=Counter(o)
		# s = max(number.values())
		# i = number.values().index(s)
		# move=int(number.items()[i][0])
		# ones = pic(move)
		# if(ones==None):
		# 	play=False
		# # else:
			# screen.blit(ones,(760,350))


		# screen.blit(image, (1200,520))
		pygame.display.update()

		if(click[0]==1):
			if(1800>mouse[0]>1700 and 70>mouse[1]>20):
				sys.exit()

		if(click[0]==1):
			if(1650>mouse[0]>1550 and 70>mouse[1]>20):
				logic.main()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
