from random import randint
from time import sleep

from p4.board import Board
from p4.utils.vector import Vector
from p4.utils.token import Token
from p4.utils.color import Color

from p4.display.helpMenu import displayHelp
from p4.display.gameView import displayGame, displayBoard

from p4.functions import tokenToString
from p4.strikeDetector import detectStrike

board = Board()

playing = True

footer = ""

tour = Token.YELLOW

# ==== Functions ====

def userInput():
	global playing
	global tour
	global footer

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
			footer = Color.RED + "Nombre invalide: le nombre doit être un entier compris entre 1 et 7"
		else:
			return value

	else:
		footer = Color.RED + "Argument invalide"

# ==== Main loop ====

while playing:

	displayGame(board, footer, tour)

	footer = ""

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
		displayBoard(board)
		print(f"\nJoueur {tokenToString(tour)} a gagné!")

	if tour == Token.YELLOW:
		tour = Token.BLUE
	else: tour = Token.YELLOW
