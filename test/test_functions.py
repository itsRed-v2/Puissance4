from p4.board import Board

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