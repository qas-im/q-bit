import pygame
import random

from pygame.locals import *


class seed(object)
	"""
	this class will be the seed for any object appearing in the game
	it will contain the coordinates of the object, the sprite(s), the
	controls, and any interactions with other types of objects
	"""

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def controls(self):
		pass

	def collision_check(self, collider):
		pass
