from p4.board import Board
from p4.utils.token import Token

def test_newBoard():
	board = Board()

	emptyColumn = [
		Token.EMPTY,
		Token.EMPTY,
		Token.EMPTY,
		Token.EMPTY,
		Token.EMPTY,
		Token.EMPTY
	]

	for i in range(Board.WIDTH):
		assert board.getColumn(i) == emptyColumn

def test_newBoardFromString():
	stringBoard = [
		"       ",
		"       ",
		"    w  ",
		"     X ",
		" XO    ",
		"OOXX O "
	]
	board = Board(stringBoard)

	assert board.getColumn(0) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.BLUE]
	assert board.getColumn(1) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.YELLOW, Token.BLUE]
	assert board.getColumn(2) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.BLUE, Token.YELLOW]
	assert board.getColumn(3) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.YELLOW]
	assert board.getColumn(4) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY]
	assert board.getColumn(5) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.YELLOW, Token.EMPTY, Token.BLUE]
	assert board.getColumn(6) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY]

	stringBoard = [
		"       ",
		"       ",
		"    O  ",
		"   .O  ",
		" XOOO  ",
		"OOXXXX "
	]
	board = Board(stringBoard)

	assert board.getColumn(0) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.BLUE]
	assert board.getColumn(1) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.YELLOW, Token.BLUE]
	assert board.getColumn(2) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.BLUE, Token.YELLOW]
	assert board.getColumn(3) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.BLUE, Token.YELLOW]
	assert board.getColumn(4) == [Token.EMPTY, Token.EMPTY, Token.BLUE, Token.BLUE, Token.BLUE, Token.YELLOW]
	assert board.getColumn(5) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.YELLOW]
	assert board.getColumn(6) == [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY]

def test_getColumn():
	board = Board()

	assert board.getColumn(-1) == None
	assert board.getColumn(Board.WIDTH) == None

def test_addToken():
	board = Board()

	board.columns[0] = [
		Token.EMPTY,
		Token.EMPTY,
		Token.EMPTY,
		Token.EMPTY,
		Token.YELLOW,
		Token.BLUE
	]
	assert board.addToken(0, Token.YELLOW) == 3
	assert board.getColumn(0) == [
		Token.EMPTY,
		Token.EMPTY,
		Token.EMPTY,
		Token.YELLOW,
		Token.YELLOW,
		Token.BLUE
	]
	assert board.addToken(0, Token.BLUE) == 2
	assert board.getColumn(0) == [
		Token.EMPTY,
		Token.EMPTY,
		Token.BLUE,
		Token.YELLOW,
		Token.YELLOW,
		Token.BLUE
	]

	board.columns[1] = [
		Token.BLUE,
		Token.BLUE,
		Token.BLUE,
		Token.YELLOW,
		Token.YELLOW,
		Token.BLUE
	]
	assert board.addToken(1, Token.YELLOW) == -1
	assert board.getColumn(1) == [
		Token.BLUE,
		Token.BLUE,
		Token.BLUE,
		Token.YELLOW,
		Token.YELLOW,
		Token.BLUE
	]