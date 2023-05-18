import pygame as pg
import sys
import os
import random as rd
from source.main_class import *
from source.func import *
from source.config import *

class MAIN:

	def __init__(self):
		pg.init()
		pg.font.init()
		pg.mixer.init()
		self.idx = 0
		self.frame_count = 0
		self.fps = 60
		self.game_over = False
		self.score = 0
		self.word_list = []
		self.stage = 1
		self.running = True

		self.cl = pg.time.Clock()
		pg.display.set_caption('BEWAN')
		self.font_space = pg.font.Font(os.path.join('asset','font','Zyana.ttf'),20)
		self.font_enter = pg.font.Font(os.path.join('asset','font','Zyana.ttf'),50)
		self.font_ent_main = pg.font.Font(os.path.join('asset','font','Zyana.ttf'),30)
		self.font_small = pg.font.Font(os.path.join('asset','font','Vermin.otf'),25)
		self.font_big = pg.font.Font(os.path.join('asset','font','Vermin.otf'),40)
		self.font_big2 = pg.font.Font(os.path.join('asset','font','Vermin.otf'),50)
		self.font_big3 = pg.font.Font(os.path.join('asset','font','Vermin.otf'),70)
		self.font_title = pg.font.Font(os.path.join('asset','font','Vermin.otf'),85)

		# load asset bg 
		self.bg = pg.image.load(os.path.join('asset', 'background', 'bg-main.png'))
		self.bg_main = pg.transform.scale(self.bg, (width, height))
		self.bg = pg.image.load(os.path.join('asset', 'background', 'bg-menu.jpg'))
		self.bg_menu = pg.transform.scale(self.bg, (width,height))

		# load music and sound
		self.fire_sound = pg.mixer.Sound(os.path.join('asset','sound','Fire_Sound_Effect.mp3'))
		self.typed_sound = pg.mixer.Sound(os.path.join('asset','sound','single_type.wav'))
		self.go_sound = pg.mixer.Sound(os.path.join('asset','sound','go-sound.mp3'))
		self.pressed_sound = pg.mixer.Sound(os.path.join('asset','sound','pressed-sound.mp3'))
		self.wrong_sound = pg.mixer.Sound(os.path.join('asset','sound','wrong-sound.mp3'))

		# load hunter before fire
		self.hunter = pg.image.load(os.path.join('asset', 'hunter', 'jeta.png'))
		self.hunter = pg.transform.flip(self.hunter, True, False)
		self.hunt_scale = (int(self.hunter.get_width() * 1) , int(self.hunter.get_height() * 1))
		self.hunter = pg.transform.scale(self.hunter, self.hunt_scale).convert_alpha()

		# load hunter firing
		self.hunter_fire = pg.image.load(os.path.join('asset', 'hunter', 'jeta_fire.png'))
		#self.hunter_fire = pg.transform.flip(self.hunter_fire, True, False)
		self.hunt_f_scale = (int(self.hunter_fire.get_width() * 1) , int(self.hunter_fire.get_height() * 1))
		self.hunter_fire = pg.transform.scale(self.hunter_fire, self.hunt_f_scale).convert_alpha()

		# load board and redline
		self.score_board_load = pg.image.load(os.path.join('asset','board','score-board.png'))
		self.board_scale = (int(self.score_board_load.get_width() * 0.29) , int(self.score_board_load.get_height() * 0.22))
		self.score_board = pg.transform.scale(self.score_board_load, self.board_scale).convert_alpha()
		self.board_scale = (int(self.score_board_load.get_width() * 0.25) , int(self.score_board_load.get_height() * 0.22))
		self.stage_board = pg.transform.scale(self.score_board_load, self.board_scale).convert_alpha()
		self.redline_load = pg.image.load(os.path.join('asset','board','redline.png'))
		self.redline_scale = (int(self.redline_load.get_width() * 1) , int(self.redline_load.get_height() * 1))
		self.redline= pg.transform.scale(self.redline_load, self.redline_scale).convert_alpha()
		self.redline.set_alpha(130)
		
		self.bewan_board_load = pg.image.load(os.path.join('asset','board','bewan-board.png'))
		self.bewan_board_scale = (int(self.bewan_board_load.get_width() * 0.28) , int(self.bewan_board_load.get_height() * 0.2))
		self.bewan_board = pg.transform.scale(self.bewan_board_load, self.bewan_board_scale).convert_alpha()

		self.h_score_board_load = pg.image.load(os.path.join('asset','board','h-score-board.png'))
		self.h_board_scale = (int(self.h_score_board_load.get_width() * 0.35) , int(self.h_score_board_load.get_height() * 0.3))
		self.high_score_board = pg.transform.scale(self.h_score_board_load, self.h_board_scale).convert_alpha()
		
		self.version_board_load = pg.image.load(os.path.join('asset','board','version-board.png'))
		self.version_board_scale = (int(self.version_board_load.get_width() * 0.2) , int(self.version_board_load.get_height() * 0.16))
		self.version_board = pg.transform.scale(self.version_board_load, self.version_board_scale).convert_alpha()

		self.go_board_load = pg.image.load(os.path.join('asset','board','go-board.png'))
		self.go_board_scale = (int(self.go_board_load.get_width() * 0.7) , int(self.go_board_load.get_height() * 0.8))
		self.go_board = pg.transform.scale(self.go_board_load, self.go_board_scale).convert_alpha()


		self.load_asset_bird = LOAD()
		self.load_asset_bird.load_asset()

		self.menu()

	def menu(self):
		
		self.menu_music = pg.mixer.music.load(os.path.join('asset','sound','menu-music.mp3'))
		pg.mixer.music.play(-1)
		pg.mixer.music.set_volume(0.5)
		self.txt = open('data-score.txt','r')
		self.txt_h_score = self.txt.read()

		self.all = []
		for self.i in range(20):
				self.all.append(WORD(self.load_asset_bird, -1))

		for self.wrd in self.all:
			self.wrd.word = ' '
			self.wrd.speed = rd.uniform(3,15)

		while True:
			
			screen.blit(self.bg_menu, (0,0))

			for self.img in self.all:
				self.img.display()
				if self.img.x < -50:
					self.img.x = width+100

			self.press_enter = self.font_enter.render("Press Enter to play", True, black)
			self.press_enter_rect = self.press_enter.get_rect()
			self.press_enter_rect.center = (width // 2, (height // 2)-130)
			screen.blit(self.press_enter, self.press_enter_rect)

			self.press_space = self.font_space.render("Press Space to reset High Scores", True, black)
			self.press_space_rect = self.press_space.get_rect()
			self.press_space_rect.center = (width // 2, (height // 2)-30)
			screen.blit(self.press_space, self.press_space_rect)

			self.h_score_rect = self.high_score_board.get_rect()
			self.h_score_rect.center = (width // 2, (height // 2)+150)
			screen.blit(self.high_score_board, self.h_score_rect)
			
			self.h_score_bar = self.font_big2.render("High Scores", True, white)
			self.h_score_val = self.font_big3.render(f"{self.txt_h_score}", True, white)
			
			self.h_score_bar_rect = self.h_score_bar.get_rect()
			self.h_score_bar_rect.center = (width // 2, (height // 2)+100)
			screen.blit(self.h_score_bar, self.h_score_bar_rect)

			self.h_score_val_rect = self.h_score_val.get_rect()
			self.h_score_val_rect.center = (width // 2, (height // 2)+190)
			screen.blit(self.h_score_val, self.h_score_val_rect)

			self.version_bar = self.font_small.render("version  1.0", True, white)
			screen.blit(self.version_board, (960,height-90))
			screen.blit(self.version_bar, (1025,height-60))

			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.mixer.music.stop()
					pg.quit()
					sys.exit()

				if event.type == pg.KEYDOWN:
					if event.key == pg.K_RETURN:
						pg.mixer.music.stop()
						self.pressed_sound.play()
						self.start()
					if event.key == pg.K_SPACE:
						self.pressed_sound.play()
						self.txt = open('data-score.txt','w')
						self.txt.write('0')
						self.txt = open('data-score.txt','r')
						self.txt_h_score = self.txt.read()

			pg.display.update()
			self.cl.tick(self.fps)

	def game_over_show(self):

		self.go_board_rect = self.go_board.get_rect()
		self.go_board_rect.center = (width // 2, (height // 2)-85)
		screen.blit(self.go_board, self.go_board_rect)

		self.go_bar = self.font_big3.render("GAME OVER", True, white)
		self.go_bar_rect = self.go_bar.get_rect()
		self.go_bar_rect.center = (width // 2, (height // 2)-100)
		screen.blit(self.go_bar, self.go_bar_rect)

		self.press_enter_menu = self.font_ent_main.render("Press  Enter ", True, white)
		self.press_enter_menu_rect = self.press_enter_menu.get_rect()
		self.press_enter_menu_rect.center = (width // 2, (height // 2)-20)
		screen.blit(self.press_enter_menu, self.press_enter_menu_rect)


	def __correct(self,word):
		word = list(word)
		word.pop(0)
		word = ''.join(word)
		return word

	def __word_empty(self,word):
		return len(word) == 0

	def start(self):
		pg.mixer.music.load(os.path.join('asset','sound','main-music.mp3'))
		pg.time.delay(1000)
		pg.mixer.music.play(-1)
		pg.mixer.music.set_volume(0.4)

		# Game Loop
		while self.running:

			self.lwl = len(self.word_list)
			
			if self.lwl > 0 and self.idx < self.lwl:
				self.word_list[self.idx].color = orange

			# adding word to list
			if self.lwl < 6: 
				if self.stage < 4:
					if self.frame_count % 100 == 0:
						self.word_list.append(WORD(self.load_asset_bird))
				elif self.stage < 8:
					if self.frame_count % 80 == 0:
						self.word_list.append(WORD(self.load_asset_bird))
				elif self.stage < 10:
					if self.frame_count % 60 == 0:
						self.word_list.append(WORD(self.load_asset_bird))
				else:
					if self.frame_count % 40 == 0:
						self.word_list.append(WORD(self.load_asset_bird))

			
			# tampilkan bg dan hewan
			screen.blit(self.bg_main, (0,0))
			screen.blit(self.hunter,(10,380))
			screen.blit(self.score_board,(770,490))
			screen.blit(self.stage_board, (400, 490))
			self.redline.set_alpha(150)
			screen.blit(self.redline, (-520,0))

			# tampilan word
			for word in self.word_list:
				if word.x > -50 and not self.game_over:
					if self.stage == 1:
						word.display()
					elif self.stage == 2:
						word.speed = 2.5
						word.display()
					elif self.stage == 3:
						word.speed = 3
						word.display()
					elif self.stage == 4:
						word.speed = 3.5
						word.display()
					elif self.stage == 5:
						word.speed = 4
						word.display()
					elif self.stage == 6:
						word.speed = 4.5
						word.display()
					elif self.stage == 7:
						word.speed = 5
						word.display()	
					elif self.stage == 8:
						word.speed = 5.5
						word.display()
					elif self.stage == 9:
						word.speed = 6
						word.display()
					elif self.stage == 10:
						word.speed = 7
						word.display()
					elif self.stage == 11:
						word.speed = 8
						word.display()
					elif self.stage == 12:
						word.speed = 9
						word.display()
					else:
						word.speed = 10
						word.display()
				
				if word.x < 0 and not self.__word_empty(word.word):
					if not self.game_over:
						self.go_sound.play()
					self.game_over  = True

			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.mixer.music.stop()
					self.txt_bef = open('data-score.txt','r')
					self.txt_bef_val = int(self.txt_bef.read())
					
					if self.score >= self.txt_bef_val:
						self.txt = open('data-score.txt','w')
						self.txt.write(str(self.score))

					self.running = False
					pg.quit()
					sys.exit()

				if event.type == pg.KEYDOWN:
					word = self.word_list

					if event.key == pg.K_RETURN and self.game_over:
						self.pressed_sound.play()
						
						# making high score update
						self.txt_bef = open('data-score.txt','r')
						self.txt_bef_val = int(self.txt_bef.read())
						
						if self.score >= self.txt_bef_val:
							self.txt = open('data-score.txt','w')
							self.txt.write(str(self.score))

						self.idx = 0
						self.frame_count = 0
						self.game_over = False
						self.score = 0
						self.word_list = []
						self.stage = 1
						self.running = True
						gen_word()
						pg.mixer.music.stop()
						self.menu()

					if event.unicode == word[self.idx].word[0]:
						word[self.idx].word = self.__correct(word[self.idx].word)
						self.typed_sound.play()
						if self.__word_empty(word[self.idx].word):
							self.score += 10
							self.idx += 1
							self.fire_sound.set_volume(1)
							self.fire_sound.play()
							
							screen.blit(self.hunter_fire, (10, 380))
							break
					else:
						self.wrong_sound.play()

			if self.game_over:
				pg.mixer.music.set_volume(0.1)
				self.game_over_show()

			if self.score != 0  and self.score % 60 == 0:
				if self.lwl == 6:
					self.word_list = []
					self.idx = 0
					self.stage += 1
					gen_word()

			self.score_bar = self.font_big.render("Score", True, white)
			self.score_value = self.font_big2.render(f"{self.score}", True, white)
			screen.blit(self.score_bar, (850,515))
			screen.blit(self.score_value, (1030,510))

			self.stage_bar = self.font_big.render("Stage", True, white)
			self.stage_value = self.font_big2.render(f"{self.stage}", True, white)
			screen.blit(self.stage_bar, (470,515))
			screen.blit(self.stage_value, (650,510))
			
			self.frame_count += 1
			pg.display.flip()
			self.cl.tick(self.fps)  # 60 fps

play = MAIN()