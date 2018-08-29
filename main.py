import pygame
import random

from time import sleep
from pygame.locals import *
from seed.seed import Seed

class Game(object):
	
	def __init__(self):
		# initialize screen and mixer
		pygame.init()
		pygame.mixer.init()
		width, height = 640,480
		self.screen = pygame.display.set_mode((width,height))
		self.player = Seed()

	def run(self):
		while True:
			sleep(0.05)
			self.screen.fill(0)
			self.player.update()


if __name__ == "__main__":
	Game().run()
