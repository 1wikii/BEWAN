from random import randrange
from source.main_class import *


def correct(word):
	word = list(word)
	word.pop(0)
	word = ''.join(word)
	return word

def word_empty(word):
	return len(word) == 0

def make_object():
	return EACH_WORD()