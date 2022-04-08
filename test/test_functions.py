from p4.board import Board

def test_getFirstEmpty():
	board = Board([
		"  O",
		" XX",
		" OO",
		" XX",
		"XXX",
		"OOO"
	], 6, 3)

	assert board.getFirstEmpty(-1) == None
	assert board.getFirstEmpty(0) == 3
	assert board.getFirstEmpty(1) == 0
	assert board.getFirstEmpty(2) == -1
	assert board.getFirstEmpty(3) == None