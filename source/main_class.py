import pygame as pg
import random as rd
from random import randrange as rr
from source.variables import *

pg.font.init()

# Configuration
width = 720
height = 500
screen = pg.display.set_mode((width,height))
cl = pg.time.Clock()
pg.display.set_caption('BEWAN')
font = pg.font.SysFont('comicsansms',36)


# Handling each word manipulation
class EACH_WORD:

	def __init__(self):
		self.x = (width + 30)
		self.y = rr(50 , (height - 200))

		self.__color = black
		self.__speed = 1.2
		self.word = rd.choice(all_word)

		# remove word if already in use avoid duplicate displayed word
		all_word.remove(self.word)

	@property
	def color(self):
		return self.__color

	def been_typed(self):
		self.__color = orange

	def moving(self):
		self.x -= self.__speed
	
	# abstraction concept hiding another method to make it simple
	def display(self):
		show_word = font.render(self.word, True, self.color)
		screen.blit(show_word, (self.x,self.y))



