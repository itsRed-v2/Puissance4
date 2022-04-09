from random import randint
from time import sleep

from p4.players.player import Player

from p4.strikeDetector import detectStrike
from p4.utils.vector import Vector
from p4.utils.token import Token

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

		playable = list(filter(filterFull, playable))

		# Joue les coups qui font gagner

		for colIndex in playable:
			pos = Vector(colIndex, board.getFirstEmpty(colIndex))
			if detectStrike(board, pos, self.token):
				return colIndex + 1
		
		# Bloque les lignes de l'adversaire

		for colIndex in playable:
			pos = Vector(colIndex, board.getFirstEmpty(colIndex))
			if detectStrike(board, pos, Token.getOpposite(self.token)):
				return colIndex + 1

		# Selection au hasard
		return playable[randint(0, len(playable) - 1)] + 1
