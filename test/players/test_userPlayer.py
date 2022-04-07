from unittest.mock import MagicMock, Mock

from p4.board import Board
from p4.display.gameView import View

from p4.players.userPlayer import UserPlayer

from p4.utils.color import Color
from p4.utils.token import Token

class MochView():
	def __init__(self):
		self.footer = ""
		self.displayGame = MagicMock()

def test_constructor():
	board = Board()
	mockView = View(board)

	def mockStopHook():
		return 24
	
	player = UserPlayer(Token.BLUE, "PLAYER", mockView, mockStopHook)

	assert player.token == Token.BLUE
	assert player.displayName == "PLAYER" + Color.RESET
	assert player.view == mockView
	assert player.stopHook() == 24

EXPECTED_DISPLAY_NAME = "PLAYER" + Color.RESET

hook = False
input = []

board = Board()
mockView = MochView()

def mockStopHook():
	global hook
	hook = True

def mockInput(string):
	returnValue = input[0]
	del input[0]
	return returnValue

player = UserPlayer(Token.BLUE, "PLAYER", mockView, mockStopHook)

def test_input_stop():
	global hook
	global input

	hook = False
	input = ["stop"]

	answer = player.play(board, mockInput)
	assert answer == None
	assert mockView.footer == ""
	assert hook == True
	mockView.displayGame.assert_not_called()

def test_input_number():
	global hook
	global input

	hook = False
	input = ["5"]

	answer = player.play(board, mockInput)
	assert answer == 5
	assert mockView.footer == ""
	assert hook == False
	mockView.displayGame.assert_not_called()

def test_input_invalid_number():
	global hook
	global input

	input = ["8", "5"]
	mockView.displayGame.reset_mock()

	answer = player.play(board, mockInput)
	assert answer == 5
	assert mockView.footer == Color.RED + "Il n'y a pas de colonne n°8"
	assert hook == False
	mockView.displayGame.assert_called_once_with(EXPECTED_DISPLAY_NAME)

	input = ["0", "2"]
	mockView.displayGame.reset_mock()

	answer = player.play(board, mockInput)
	assert answer == 2
	assert mockView.footer == Color.RED + "Il n'y a pas de colonne n°0"
	assert hook == False
	mockView.displayGame.assert_called_once()

def test_invalid_input():
	global hook
	global input

	input = ["blblbl", "5"]
	mockView.displayGame.reset_mock()

	answer = player.play(board, mockInput)
	assert answer == 5
	assert mockView.footer == Color.RED + "Argument invalide"
	assert hook == False
	mockView.displayGame.assert_called_once()

def test_input_full_column():
	global hook
	global input
	global board

	board.columns[4] = [
		Token.BLUE,
		Token.YELLOW,
		Token.YELLOW,
		Token.BLUE,
		Token.BLUE,
		Token.YELLOW
	]

	input = ["5", "3"]
	mockView.displayGame.reset_mock()

	answer = player.play(board, mockInput)
	assert answer == 3
	assert mockView.footer == Color.RED + "Cette colonne est pleine!"
	assert hook == False
	mockView.displayGame.assert_called_once()

	board = Board()

def test_empty_input():
	global hook
	global input

	mockView.footer = ""
	mockView.displayGame.reset_mock()

	input = ["", "7"]

	answer = player.play(board, mockInput)
	assert answer == 7 
	assert mockView.footer == ""
	assert hook == False
	mockView.displayGame.assert_called_once()

def test_help_input():
	global hook
	global input

	mockView.displayGame.reset_mock()
	mockDisplayHelp = Mock()

	input = ["help", "1"]

	answer = player.play(board, mockInput, mockDisplayHelp)
	assert answer == 1 
	assert mockView.footer == ""
	assert hook == False
	mockView.displayGame.assert_called_once()
	mockDisplayHelp.assert_called_once()