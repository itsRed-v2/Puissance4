from random import randint
from time import sleep

from p4.players.player import Player

class IAPlayer(Player):
	def play(self, board, randint = randint, doSleep = True):
		if doSleep: sleep(.5)

		# Initialisation
		playable = []
		for i in range(board.WIDTH):
			playable.append(i)

		# Suppression des colonnes pleines

		def filterFull(colIndex):
			firstEmpty = board.getFirstEmpty(colIndex)
			return firstEmpty != None and firstEmpty != -1

		playable = filter(filterFull, playable)

		# Selection au hasard
		playable = list(playable)
		return playable[randint(0, len(playable) - 1)] + 1
