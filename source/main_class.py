import pygame as pg
import random as rd
import os
from random import randrange as rr
from source.config import *
from abc import ABC, abstractmethod

all_word = ['burung-hantu','kakak-tua','burung-cinta','elang','gagak','merpati']

def gen_word():
	global all_word
	all_word.append('burung-hantu')
	all_word.append('kakak-tua')
	all_word.append('burung-cinta')
	all_word.append('elang')
	all_word.append('gagak')
	all_word.append('merpati')

class LIST_WORD(ABC):

	def __init__(self):
		self.all_animal = []

	@abstractmethod
	def load_asset(self):
		pass
		
class LOAD(LIST_WORD):

	def __init__(self):
		super().__init__()
		self.list_b_hantu = []
		self.list_elang = []
		self.list_gagak = []
		self.list_kk_tua = []
		self.list_love_b = []
		self.list_merpati = []

	# POLYMORPHISM OVERIDING (nama fungsi sama dengan action berbeda)
	def load_asset(self):
		self.list_b_hantu.append(pg.image.load(os.path.join("asset","birds","burung_hantu1.png")).convert_alpha())
		self.list_b_hantu.append(pg.image.load(os.path.join("asset","birds","burung_hantu4.png")).convert_alpha())
		self.list_elang.append(pg.image.load(os.path.join("asset","birds","elang3.png")).convert_alpha())
		self.list_elang.append(pg.image.load(os.path.join("asset","birds","elang3.png")).convert_alpha())
		self.list_gagak.append(pg.image.load(os.path.join("asset","birds","gagak1.png")).convert_alpha())
		self.list_gagak.append(pg.image.load(os.path.join("asset","birds","gagak4.png")).convert_alpha())
		self.list_kk_tua.append(pg.image.load(os.path.join("asset","birds","kakaktua1.png")).convert_alpha())
		self.list_kk_tua.append(pg.image.load(os.path.join("asset","birds","kakaktua2.png")).convert_alpha())
		self.list_love_b.append(pg.image.load(os.path.join("asset","birds","love-bird1.png")).convert_alpha())
		self.list_love_b.append(pg.image.load(os.path.join("asset","birds","love-bird3.png")).convert_alpha())
		self.list_merpati.append(pg.image.load(os.path.join("asset","birds","merpati1.png")).convert_alpha())
		self.list_merpati.append(pg.image.load(os.path.join("asset","birds","merpati3.png")).convert_alpha())

		self.all_animal.append(self.list_b_hantu)
		self.all_animal.append(self.list_elang)
		self.all_animal.append(self.list_gagak)
		self.all_animal.append(self.list_kk_tua)
		self.all_animal.append(self.list_merpati)
		self.all_animal.append(self.list_love_b)


# Handling each word manipulation
class WORD(LOAD):

	def __init__(self, objek, rnd=0):
		super().__init__()
		pg.font.init()
		self.all_animal = objek.all_animal
		self.font = pg.font.SysFont('comicsansms',36)
		self.rnd = rnd

		if (rnd == 0):
			self.x = (width + 30)
		else:
			self.x = rr(-100, 400)
		self.y = rr(80 , (height - 250))

		self.__color = white
		self.__speed = 2

		self.index_img = rr(0,number_of_bird)
		self.img_csn = self.all_animal[self.index_img]
		#self.img_up = self.img_csn[0]
		self.img_down = self.img_csn[1]

		# remove word if already in use avoid duplicate displayed word
		if rnd == 0:
			self.word = rd.choice(all_word)
			all_word.remove(self.word)

		self.load_asset()

	@property
	def color(self):
		return self.__color

	@color.setter
	def color(self, value):
		self.__color = value

	@property
	def speed(self):
		return self.__speed
	
	@speed.setter
	def speed(self, value):
		self.__speed = value

	def moving(self):
		self.x -= self.__speed


	# POLYMORPHISM OVERIDING (nama fungsi sama dengan action berbeda)
	def load_asset(self):

		self.black_box_load = pg.image.load(os.path.join("asset","board","black_box.png")).convert_alpha()

		self.scale = (int(self.img_down.get_width() * 0.2) , int(self.img_down.get_height() * 0.2))
		self.down = pg.transform.scale(self.img_down, self.scale).convert_alpha()

	def scaling_black_box(self, word_width):
		#self.black_box_scale = (int(self.black_box_load.get_width() * 0.5) , int(self.black_box_load.get_height() * 0.5))
		self.black_box_scale = ( word_width+55, int(self.black_box_load.get_height() * 0.15))
		self.black_box = pg.transform.scale(self.black_box_load, self.black_box_scale).convert_alpha()
	
	
	def display(self):
		self.moving()

		if len(self.word) != 0 :
			screen.blit(self.down, (self.x-50,self.y-150))
		elif(len(self.word) > 7) :
			screen.blit(self.down, (self.x-100,self.y-150))

		self.show_word = self.font.render(self.word, True, self.color)
		self.scaling_black_box(self.show_word.get_width())

		if self.rnd == 0 and len(self.word) != 0:
			self.tran = int((80 / 100) * 255)
			self.black_box.set_alpha(self.tran)
			screen.blit(self.black_box, (self.x-26,self.y))
		
		
		screen.blit(self.show_word, (self.x,self.y))
		
		



