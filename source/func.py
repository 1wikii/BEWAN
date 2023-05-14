from source.config import *

def correct(word):
	word = list(word)
	word.pop(0)
	word = ''.join(word)
	return word

def word_empty(word):
	return len(word) == 0