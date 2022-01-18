from random import randint
from time import sleep

from p4.board import Board
from p4.utils.vector import Vector
from p4.utils.token import Token
from p4.utils.color import Color

from p4.display.helpMenu import displayHelp
from p4.display.gameView import View

from p4.functions import getFirstEmpty, tokenToString
from p4.strikeDetector import detectStrike

board = Board()

view = View(board)

playing = True

tour = Token.YELLOW

# ==== Functions ====

def userInput():
	global view
	global playing
	global tour

	reponse = input("-> ")

	if reponse == "":
		return

	elif reponse == "stop":
		playing = False

	elif reponse == "help":
		displayHelp()

	elif reponse.isdecimal():
		value = int(reponse)

		if value < 1 or value > 7:
			view.footer = Color.RED + "Il n'y a pas de colonne n°" + reponse
		elif getFirstEmpty(board.getColumn(value - 1)) == -1:
			view.footer = Color.RED + "Cette colonne est pleine!"
			return value
		else:
			return value

	else:
		view.footer = Color.RED + "Argument invalide"

# ==== Main loop ====

while playing:

	view.displayGame(tour)

	match tour:
		case Token.YELLOW:
			answer = userInput()
		case Token.BLUE:
			sleep(1)
			answer = randint(1, Board.WIDTH)

	if not type(answer) is int:
		continue

	row = board.addToken(answer - 1, tour)

	if row == -1 or row == None:
		continue

	if detectStrike(board, Vector(answer - 1, row), tour):
		playing = False

		print(Color.RESET + "\n")
		view.displayBoard()
		print(f"\nJoueur {tokenToString(tour)} a gagné!")

	tour = (Token.BLUE if tour == Token.YELLOW else Token.YELLOW)