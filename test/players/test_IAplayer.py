from p4.board import Board

from p4.players.IAplayer import IAPlayer

from p4.utils.token import Token

def test_randomPlay():
	IA = IAPlayer(Token.BLUE, "IA")

	board = Board([
		"       ",
		"       ",
		"       ",
		"       ",
		"BY   B ",
		"YYBBYYB"
	])

	randomRuns = 0

	def mockRandom(a, b):
		nonlocal randomRuns
		randomRuns += 1
		assert a == 0
		assert b == 6
		return 0

	assert IA.play(board, mockRandom, False) == 1
	assert randomRuns == 1

def test_fullColumns():
	IA = IAPlayer(Token.BLUE, "IA")

	board = Board([
		"BBYY BY",
		"YYBBYYB",
		"BBYYBBY",
		"YYBBYYB",
		"BBYYBBY",
		"YYBBYYB"
	])

	randomRuns = 0

	def mockRandom(a, b):
		nonlocal randomRuns
		randomRuns += 1
		assert a == 0
		assert b == 0
		return 0

	assert IA.play(board, mockRandom, False) == 5
	assert randomRuns == 1

def test_win():
	IA = IAPlayer(Token.BLUE, "IA")

	board = Board([
		"       ",
		"       ",
		"       ",
		"       ",
		"BY B.BB",
		"YYBBYYB"
	])

	randomRuns = 0

	def mockRandom(a, b):
		nonlocal randomRuns
		randomRuns += 1
		return 0

	assert IA.play(board, mockRandom, False) == 5
	assert randomRuns == 0

	board = Board([
		"       ",
		"       ",
		".      ",
		"BB     ",
		"BYB    ",
		"YYBBYYB"
	])

	randomRuns = 0

	def mockRandom(a, b):
		nonlocal randomRuns
		randomRuns += 1
		return 0

	assert IA.play(board, mockRandom, False) == 1
	assert randomRuns == 0