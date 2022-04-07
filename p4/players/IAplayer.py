from random import randint
from time import sleep

from p4.players.player import Player

class IAPlayer(Player):
	def play(self, board):
		sleep(.5)
		return randint(1, board.WIDTH)
