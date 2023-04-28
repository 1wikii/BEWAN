import pygame as pg
import random as rd

# COLOR
purple = (189, 52, 235)
white = (255, 255, 255)
orange = (242, 103, 10)
black = (0, 0, 0)

# WORD LIST 
word_list = ['nangka','nanas','semangka','durian','mangga']
score = 0

# Handling each letter color
class EACH_WORD:

	def __init__(self):
		self.__color = black
		self.word = rd.choice(word_list)
	
	@property
	def color(self):
		return self.__color

	def typed(self):
		self.__color = orange

	def move_to_right(self):
		pass

	def move_to_left(self):
		pass
	
	# abstraction concept hiding another method to make it simple
	def word_moving(self, direction):
		if direction == "right":
			self.move_to_right()
		
		elif direction == "left":
			self.move_to_left()


def correct(word):
	word = list(word)
	word.pop(0)
	word = ''.join(word)
	return word

def word_empty(word):
	return len(word) == 0

def make_obj():
	return EACH_WORD()

pg.init()
screen = pg.display.set_mode((720,500))
cl = pg.time.Clock()
pg.display.set_caption('BEWAN')
font = pg.font.SysFont('comicsansms',36)
running = True

main_word = make_obj()
the_word = main_word.word

while running:

	screen.fill("purple")

	show = font.render(the_word, True, main_word.color)
	screen.blit(show, (200,200))

	sc = font.render( f"Score : {score}", True, black)
	screen.blit (sc, (10,10))

	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False

		if event.type == pg.KEYDOWN:

			# for idx in range(len(the_word)):
			if chr(event.key) == the_word[0]:
				the_word = correct(the_word)
				if word_empty(the_word):
					main_word = make_obj()
					the_word = main_word.word
					score += 1
	
	pg.display.update()
	cl.tick(60)  # 60 fps
