from p4.players.IAplayer import IAPlayer
from p4.players.userPlayer import UserPlayer

from p4.board import Board
from p4.utils.token import Token
from p4.utils.vector import Vector
from p4.utils.color import Color

from p4.display.gameView import View

from p4.strikeDetector import detectStrike

board = Board()

view = View(board)

def stopGame():
	global playing
	playing = False

USER = UserPlayer(Token.YELLOW, Color.YELLOW + "JAUNE", view, stopGame)
IA = IAPlayer(Token.BLUE, Color.BLUE + "BLEU")

playing = True

# ==== Functions ====

def play(player):
	answer = player.play(board)

	if answer == None:
		return False

	row = board.addToken(answer - 1, player.token)

	if row == -1 or row == None:
		return False

	if detectStrike(board, Vector(answer - 1, row), player.token):
		stopGame()
		view.display_win(player.displayName)

	return True

# ==== Main loop ====

view.displayGame(USER.displayName)
play(USER)

while playing:

	view.displayGame(IA.displayName)
	if not play(IA):
		print(Color.RED + "AI played wrong!!")
		playing = False

	view.displayGame(USER.displayName)
	play(USER)