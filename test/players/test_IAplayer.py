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
		assert a == 0
		assert b == 0
		return 0

	assert IA.play(board, mockRandom, False) == 5
	assert randomRuns == 1

	board = Board([
		"       ",
		"       ",
		"     . ",
		" Y  BB ",
		" Y BYY ",
		"YYBBYYB"
	])

	randomRuns = 0

	def mockRandom(a, b):
		nonlocal randomRuns
		randomRuns += 1
		assert a == 0
		assert b == 0
		return 0

	assert IA.play(board, mockRandom, False) == 6
	assert randomRuns == 1

def test_block():
	IA = IAPlayer(Token.YELLOW, "IA")

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
		assert a == 0
		assert b == 0
		return 0

	assert IA.play(board, mockRandom, False) == 5
	assert randomRuns == 1

	board = Board([
		"       ",
		"       ",
		"     . ",
		"    BB ",
		" Y BYY ",
		"YYBBYYB"
	])

	randomRuns = 0
	
	def mockRandom(a, b):
		nonlocal randomRuns
		randomRuns += 1
		assert a == 0
		assert b == 0
		return 0

	assert IA.play(board, mockRandom, False) == 6
	assert randomRuns == 1

def test_unsafeBlock():
	IA = IAPlayer(Token.BLUE, "IA")

	board = Board([
		"       ",
		"       ",
		" .     ",
		"xB     ",
		"BYB    ",
		"YYBBYYB"
	])

	randomRuns = 0
	
	def mockRandom(a, b):
		nonlocal randomRuns
		randomRuns += 1
		assert a == 0
		assert b == 5
		return 0

	assert IA.play(board, mockRandom, False) == 2
	assert randomRuns == 1

def test_unsafe():
	IA = IAPlayer(Token.BLUE, "IA")

	board = Board([
		"BBY B B",
		"YYY B Y",
		"YBB-B B",
		"BBY.YBY",
		"BYBBYBB",
		"YYBBYYB"
	])

	randomRuns = 0
	
	def mockRandom(a, b):
		nonlocal randomRuns
		randomRuns += 1
		assert a == 0
		assert b == 0
		return 0

	assert IA.play(board, mockRandom, False) == 6
	assert randomRuns == 1

def test_allUnsafe():
	IA = IAPlayer(Token.BLUE, "IA")

	board = Board([
		"BBY BYB",
		"YYY BYY",
		"YBB-BYB",
		"BBY.YBY",
		"BYBBYBB",
		"YYBBYYB"
	])

	randomRuns = 0
	
	def mockRandom(a, b):
		nonlocal randomRuns
		randomRuns += 1
		assert a == 0
		assert b == 0
		return 0

	assert IA.play(board, mockRandom, False) == 4
	assert randomRuns == 1