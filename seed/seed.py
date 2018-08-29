import pygame
import random

from pygame.locals import *


class Seed(object):
	"""
	this class will be the seed for any object appearing in the game
	it will contain the coordinates of the object, the sprite(s), the
	controls, and any interactions with other types of objects
	"""

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.keys = {"a":False,
					 "b":False,
					 "c":False,
					 "d":False,
					 "e":False,
					 "f":False,
					 "g":False,
					 "h":False,
					 "i":False,
					 "j":False,
					 "k":False,
					 "l":False,
					 "m":False,
					 "n":False,
					 "o":False,
					 "p":False,
					 "q":False,
					 "r":False,
					 "s":False,
					 "t":False,
					 "u":False,
					 "v":False,
					 "w":False,
					 "x":False,
					 "y":False,
					 "z":False
					 }
		self.was_pressed = False

	def key_is_pressed(self,key):
		"""
		boolean function
		true when key IS being pressed
		e.g. for holding down movement
		uses ascii values to recognise keys
		"""
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == ord(key):
					self.keys[key] = True
			if event.type == pygame.KEYUP:
				if event.key == ord(key):
					self.keys[key] = False
		return self.keys[key]

	def key_was_pressed(self,key):
		"""
		boolean function
		true when key WAS pressed
		e.g. firing a single missle per click
		uses ascii values to recognise keys
		"""
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == ord(key):
					return True
		return False

	def update(self):
		"""
		function that controls movement/actions of an object
		used in conjunction with key_xxx_pressed functions
		"""
		if self.key_is_pressed("w"):
			print("going up")
		if self.key_is_pressed("a"):
			print("going left")
		if self.key_is_pressed("s"):
			print("going down")
		if self.key_is_pressed("d"):
			print("going right")


	def collision_check(self, collider):
		pass
