from p4.utils.color import Color
from p4.utils.token import Token

def getFirstEmpty(column):
	for row in range(len(column) - 1, -1, -1): # This ranges from len(column) - 1 to 0
		if column[row] == Token.EMPTY:
			return row
	return -1

tokenNames = {
	Token.BLUE: Color.BLUE + "BLEU",
	Token.YELLOW: Color.YELLOW + "JAUNE",
	Token.EMPTY: Color.GRAY + "NONE"
}

def tokenToString(token):
	return tokenNames.get(token) + Color.RESET