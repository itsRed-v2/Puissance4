from p4.utils.token import Token

def getFirstEmpty(column):
	for row in range(len(column) - 1, -1, -1): # This ranges from len(column) - 1 to 0
		if column[row] == Token.EMPTY:
			return row
	return -1