import pygame as pg
import random as rd

pg.init()
screen = pg.display.set_mode((720,500))
cl = pg.time.Clock()
running = True

pg.display.set_caption('TYPING GAME by wikii')
screen.fill("purple")
font = pg.font.SysFont('comicsansms',36)

# COLOR
purple = (189, 52, 235)
white = (255, 255, 255)
orange = (242, 103, 10)

# WORD LIST 
word_list = ['nangka','nanas','semangka','durian']
score = 0

# Handling each letter color
class WORD:

	def __init__(self):
		self.color = white
		self.word = rd.choice(word_list)

	def typed(self):
		self.color = orange

	def left_right(self):
		pass

	def right_left(self):
		pass

	def draw(self):
		letter_surf = font.render(self.ch, True, white)
		screen.blit(letter_surf, (100,100))

def correct(word):
	word.pop(0)
	return word

def word_empty(word):
	return len(word) == 0

def make_obj():
	return WORD()

xx = screen.get_rect().width/2
yy = 400

word = make_obj()
while running:
	pos = 0
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		
		if event.type == pg.KEYDOWN:
			for idx in range(len(word)):
				if chr(event.key) == word[0].letter:
					correct(word)
				if word_empty(word):
					word = make_obj()
					score += 1
	
	sc = font.render( f"Score : {score}", True, black)
	screen.blit (sc, (10,10))
	
	pg.display.update()
	cl.tick(60)  # 60 fps
