from p4.board import Board
from p4.utils.vector import Vector
from p4.utils.token import Token
from p4.strikeDetector import detectStrike, is4Line, lineLength

def test_lineLength():
	board = Board([
		"       ",
		"       ",
		"       ",
		"       ",
		" YB    ",
		"BBYY.  "
	])
	direction = Vector(-1, 0)
	pos = Vector(4, 5)
	assert lineLength(board, pos, direction, Token.YELLOW) == 2
	assert lineLength(board, pos, direction, Token.BLUE) == 0

	board = Board([
		"       ",
		"       ",
		"    B  ",
		"   .B  ",
		" YBBB  ",
		"BBYYYY "
	])
	pos = Vector(3, 3)
	assert lineLength(board, pos, Vector(-1, 1), Token.BLUE) == 2
	assert lineLength(board, pos, Vector(1, -1), Token.BLUE) == 1

def test_isLine():
	board = Board([
		"       ",
		"       ",
		"       ",
		"       ",
		" YB    ",
		"BBYY.Y "
	])
	direction = Vector(1, 0)
	pos = Vector(4, 5)
	assert is4Line(board, pos, direction, Token.YELLOW) == True
	assert is4Line(board, pos, direction, Token.BLUE) == False

	board = Board([
		"       ",
		"       ",
		"    B  ",
		"   .B  ",
		" YBBB  ",
		"BBYYYY "
	])
	direction = Vector(1, -1)
	pos = Vector(3, 3)
	assert is4Line(board, pos, direction, Token.BLUE) == True
	assert is4Line(board, pos, direction, Token.YELLOW) == False

def test_is4Strike():
	board = Board([
		"       ",
		"       ",
		"       ",
		"       ",
		" YB    ",
		"BBYY.Y "
	])
	pos = Vector(4, 5)
	assert detectStrike(board, pos, Token.YELLOW) == True
	assert detectStrike(board, pos, Token.BLUE) == False

	board = Board([
		"       ",
		"       ",
		"    B  ",
		"   .B  ",
		" YBBB  ",
		"BBYYYY "
	])
	pos = Vector(3, 3)
	assert detectStrike(board, pos, Token.BLUE) == True
	assert detectStrike(board, pos, Token.YELLOW) == False

	board = Board([
		"       ",
		"B      ",
		" .BB   ",
		" YB    ",
		" Y     ",
		" Y  B  "
	])
	pos = Vector(1, 2)
	assert detectStrike(board, pos, Token.YELLOW) == True
	assert detectStrike(board, pos, Token.BLUE) == False