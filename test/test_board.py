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

	for i in range(7): # default width is 7
		assert board.getColumn(i) == emptyColumn

def test_newBoardSized():
	board = Board(height = 2, width = 18)

	emptyColumn = [
		Token.EMPTY,
		Token.EMPTY
	]

	for i in range(18):
		assert board.getColumn(i) == emptyColumn

def test_newBoardFromString():
	E = Token.EMPTY
	B = Token.BLUE
	Y = Token.YELLOW

	stringBoard = [
		"       ",
		"       ",
		"    w  ",
		"     Y ",
		" YB    ",
		"BBYY B "
	]
	board = Board(stringBoard)

	assert board.getColumn(0) == [E, E, E, E, E, B]
	assert board.getColumn(1) == [E, E, E, E, Y, B]
	assert board.getColumn(2) == [E, E, E, E, B, Y]
	assert board.getColumn(3) == [E, E, E, E, E, Y]
	assert board.getColumn(4) == [E, E, E, E, E, E]
	assert board.getColumn(5) == [E, E, E, Y, E, B]
	assert board.getColumn(6) == [E, E, E, E, E, E]

	stringBoard = [
		"       B",
		"    B  B",
		"   .B  Y",
		" YBBB  Y",
		"BBYYYY B"
	]
	board = Board(stringBoard, 5, 8)

	assert board.getColumn(0) == [E, E, E, E, B]
	assert board.getColumn(1) == [E, E, E, Y, B]
	assert board.getColumn(2) == [E, E, E, B, Y]
	assert board.getColumn(3) == [E, E, E, B, Y]
	assert board.getColumn(4) == [E, B, B, B, Y]
	assert board.getColumn(5) == [E, E, E, E, Y]
	assert board.getColumn(6) == [E, E, E, E, E]
	assert board.getColumn(7) == [B, B, Y, Y, B]

def test_getColumn():
	board = Board(height = 21, width = 3)

	assert board.getColumn(-1) == None
	assert board.getColumn(3) == None
	assert board.getColumn(2) == [Token.EMPTY] * 21

def test_addToken():
	E = Token.EMPTY
	B = Token.BLUE
	Y = Token.YELLOW

	board = Board()

	board.columns[0] = [E, E, E, E, Y, B]
	assert board.addToken(0, Y) == 3
	assert board.getColumn(0) == [E, E, E, Y, Y, B]

	assert board.addToken(0, B) == 2
	assert board.getColumn(0) == [E, E, B, Y, Y, B]

	board.columns[1] = [B, B, B, Y, Y, B]
	assert board.addToken(1, Y) == -1
	assert board.getColumn(1) == [B, B, B, Y, Y, B]

def test_getFirstEmpty():
	board = Board([
		"  B",
		" YY",
		" BB",
		" YY",
		"YYY",
		"BBB"
	], 6, 3)

	assert board.getFirstEmpty(-1) == None
	assert board.getFirstEmpty(0) == 3
	assert board.getFirstEmpty(1) == 0
	assert board.getFirstEmpty(2) == -1
	assert board.getFirstEmpty(3) == None