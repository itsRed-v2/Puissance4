from p4.utils.color import Color
from p4.utils.token import Token

def getFirstEmpty(column):
	for row in range(len(column) - 1, -1, -1): # This ranges from len(column) - 1 to 0
		if column[row] == Token.EMPTY:
			return row
	return -1

def tokenToString(token):
	if token == Token.BLUE:
		return Color.BLUE + "BLEU" + Color.RESET
	elif token == Token.YELLOW:
		return Color.YELLOW + "JAUNE" + Color.RESET
	elif token == Token.EMPTY:
		return Color.GRAY + "NONE" + Color.RESET