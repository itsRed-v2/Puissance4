from termios import VEOF
from p4.board import Board
from p4.utils.vector import Vector
from p4.utils.token import Token
from p4.strikeDetector import detectStrike, is4Line, findLine

def test_findLine():
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
	assert findLine(board, pos, direction, Token.YELLOW) == [Vector(3, 5), Vector(2, 5)]
	assert findLine(board, pos, direction, Token.BLUE) == []

	board = Board([
		"       ",
		"       ",
		"    B  ",
		"   .B  ",
		" YBBB  ",
		"BBYYYY "
	])
	pos = Vector(3, 3)
	assert findLine(board, pos, Vector(-1, 1), Token.BLUE) == [Vector(2, 4), Vector(1, 5)]
	assert findLine(board, pos, Vector(1, -1), Token.BLUE) == [Vector(4, 2)]

def test_is4Line():
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
	assert is4Line(board, pos, direction, Token.YELLOW) == [Vector(5, 5), Vector(4, 5), Vector(3, 5), Vector(2, 5)]
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
	assert is4Line(board, pos, direction, Token.BLUE) == [Vector(4, 2), Vector(3, 3), Vector(2, 4), Vector(1, 5)]
	assert is4Line(board, pos, direction, Token.YELLOW) == False

def test_detectStrike():
	board = Board([
		"       ",
		"       ",
		"       ",
		"       ",
		" YB    ",
		"BBYY.Y "
	])
	pos = Vector(4, 5)
	assert detectStrike(board, pos, Token.YELLOW) == [Vector(5, 5), Vector(4, 5), Vector(3, 5), Vector(2, 5)]
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
	assert detectStrike(board, pos, Token.BLUE) == [Vector(1, 5), Vector(2, 4), Vector(3, 3), Vector(4, 2)]
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
	assert detectStrike(board, pos, Token.YELLOW) == [Vector(1, 5), Vector(1, 4), Vector(1, 3), Vector(1, 2)]
	assert detectStrike(board, pos, Token.BLUE) == False

	board = Board([
		" Y     ",
		"BY     ",
		" .BB   ",
		" YB    ",
		" Y     ",
		" Y  B  "
	])
	pos = Vector(1, 2)
	assert detectStrike(board, pos, Token.YELLOW) == [Vector(1, 5), Vector(1, 4), Vector(1, 3), Vector(1, 2), Vector(1, 1), Vector(1, 0)]
	assert detectStrike(board, pos, Token.BLUE) == False