from p4.utils.token import Token

def test_getOpposite():
	assert Token.getOpposite(Token.BLUE) == Token.YELLOW
	assert Token.getOpposite(Token.YELLOW) == Token.BLUE

	assert Token.getOpposite(Token.EMPTY) == None
	assert Token.getOpposite("blob") == None