from p4.board import Board
from p4.utils.vector import Vector

def detectStrike(board, pos, tokenColor):

	directions = [
		Vector(1, 1),
		Vector(0, 1),
		Vector(-1, 1),
		Vector(1, 0)
	]

	for direction in directions:
		if is4Line(board, pos, direction, tokenColor):
			return True
	
	return False

def is4Line(board, pos, direction, tokenColor):
	strike = 1

	strike += lineLength(board, pos, direction, tokenColor)
	direction.multiply(-1)
	strike += lineLength(board, pos, direction, tokenColor)
	
	if strike >= 4:
		return True
	return False

def lineLength(board, pos, direction, tokenColor):
	strike = 0

	pointer = Vector(pos.c, pos.r)
	pointer.add(direction)
	
	while (0 <= pointer.c < Board.WIDTH
			and 0 <= pointer.r < Board.HEIGHT
			and board.getColumn(pointer.c)[pointer.r] == tokenColor):

		strike += 1

		pointer.add(direction)
	
	return strike