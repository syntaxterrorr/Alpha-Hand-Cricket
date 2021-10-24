import pygame,logic
import os,sys
from pygame.locals import *


def main():
	pygame.init()
	screen = pygame.display.set_mode((1920, 1080))

	clock = pygame.time.Clock()
	print("MAIN")
	while 1:
		mouse_main = pygame.mouse.get_pos()
		print(mouse_main)
		click_main = pygame.mouse.get_pressed()
		screen.fill((255, 255, 0))
		font = pygame.font.SysFont("comicsansms", 72)
		button_font = pygame.font.SysFont("comicsansms", 30)
		text = font.render("Alpha Hand-Cricket", True, (0, 128, 0))

		re_button_text = button_font.render("Replay", True, (0, 0, 0))
		ex_button_text = button_font.render("Exit", True, (0, 0, 0))

		# image = cam.get_image()
		pygame.draw.rect(screen, (0, 255, 0),(1550,20,100,50))
		screen.blit(re_button_text,(1565,35))
		pygame.draw.rect(screen, (255, 0, 0),(1700,20,100,50))
		screen.blit(ex_button_text,(1730,35))
		screen.blit(text,(760,35))

		# screen.blit(image, (1200,520))
		pygame.display.flip()

		if(click_main[0]==1):
			if(1800>mouse_main[0]>1700 and 70>mouse_main[1]>20):
				sys.exit()

		if(click_main[0]==1):
			if(1650>mouse_main[0]>1550 and 70>mouse_main[1]>20):
				logic.main()
		#
		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		sys.exit()
