# playerhand.py

import random
from poker.enumerators import Suits
from poker.card import Card

class PlayerHand(object):
	def __init__(self, card1=None, card2=None):
		self.card1 = card1
		self.card2 = card2


	def cards(self):
		return self.card1, self.card2

	def getSuits(self):
		return self.card1.suit, self.card2.suit

	def to_string(self, pretty=True):
		return self.card1.to_string(pretty=pretty) + self.card2.to_string(pretty=pretty)

	def print(self):
		print(self.to_string())
