import pygame as pg
import sys
from source.main_class import *
from source.stages import *
from source.func import *
from source.variables import *

pg.init()
#pg.mixer.init()

current_stage = stage_1

# Game Loop
while True:
	lwl = len(word_list)
	
	if lwl > 0 and idx < lwl:
		word_list[idx].been_typed()

	# adding word to list
	if lwl < current_stage['number_of_word']:
		if frame_count % 180 == 0:
			word_list.append(EACH_WORD())
	

	screen.fill("purple")
	for word in word_list:
		if word.x > -30:
			word.moving()
			word.display()

	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

		if event.type == pg.KEYDOWN:
			word = word_list
			if  event.unicode == word[idx].word[0]:
				word[idx].word = correct(word[idx].word)
		
				if word_empty(word[idx].word):
					score += 1
					idx += 1
					break


	sc = font.render( f"Score : {score}", True, red)
	screen.blit (sc, ((width/2)-100 , height-100))
	
	frame_count += 1
	pg.display.update()
	cl.tick(fps)  # 60 fps
