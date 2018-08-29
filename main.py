import pygame
import random

from pygame.locals import *


class Game(object)
	
	def __init__(self):
		# initialize screen and mixer
		pygame.init()
		pygame.mixer.init()
		width, height = 640,480
		self.screen = pygame.display.set_mode((width,height))

	def run(self):
		while true:
			self.screen.fill(0)


if __name__ == "__main__":
	Game().run()
