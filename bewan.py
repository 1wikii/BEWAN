import pygame as pg
import sys
from source.main_class import *
from source.stages import *
from source.func import *
from source.variables import *

pg.init()
#pg.mixer.init()

stage = [stage_1, stage_2, stage_3]

# Game Loop
while True:
	lwl = len(word_list)
	current = 0
	current_stage = stage[current]
	health = current_stage['number_of_word']
	
	# INI APA
	if lwl > 0 and idx < lwl:
		word_list[idx].been_typed()

	# adding word to list
	if lwl < current_stage['number_of_word']:
		if frame_count % 180 == 0:
			word_list.append(EACH_WORD())
	
	# INI APA
	screen.fill("white")
	for word in word_list:
		if word.x > -30:
			word.moving()
			word.display()
		
		if word.x < -30:
			game_over = font.render("GAME OVER", True, red)
			screen.blit(game_over, ((width / 2) - 100 , height - 300))
			break

	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

		if event.type == pg.KEYDOWN:
			word = word_list
			if event.unicode == word[idx].word[0]:
				word[idx].word = correct(word[idx].word)
		
				if word_empty(word[idx].word):
					score += 1
					idx += 1
					break

	score_bar = font.render(f"Score : {score}", True, red)
	screen.blit(score_bar, ((width / 2) - 100 , height - 100))
	level_bar = font.render(f"Level : {current + 1}", True, red)
	screen.blit(level_bar, ((width / 2) - 100 , height - 50))
	
	frame_count += 1
	pg.display.update()
	cl.tick(fps)  # 60 fps
