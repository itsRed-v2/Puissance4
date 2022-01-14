from ast import match_case
from p4.board import Board
from p4.utils.vector import Vector
from p4.utils.token import Token
from p4.utils.color import Color

from p4.display.helpMenu import displayHelp
from p4.display.gameView import displayGame, displayBoard

from p4.functions import tokenToString
from p4.strikeDetector import detectStrike

board = Board()

# ================================

playing = True

footer = ""

tour = Token.YELLOW

while playing:

	displayGame(board, footer, tour)

	footer = ""

	reponse = input("-> ")

	if reponse == "":
		continue

	elif reponse == "stop":
		playing = False

	elif reponse == "help":
		displayHelp()

	elif reponse.isdecimal():
		value = int(reponse)

		if value < 1 or value > 7:
			footer = Color.RED + "Nombre invalide: le nombre doit être un entier compris entre 1 et 7"
		else:
			l = board.addToken(value - 1, tour)

			if detectStrike(board, Vector(value - 1, l), tour):
				playing = False

				print(Color.RESET + "\n")
				displayBoard(board)
				print(f"\nJoueur {tokenToString(tour)} a gagné!")

			if tour == Token.YELLOW: 
				tour = Token.BLUE
			else: tour = Token.YELLOW

	else:
		footer = Color.RED + "Argument invalide"