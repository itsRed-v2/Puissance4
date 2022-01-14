from p4.utils.token import Token
from p4.functions import getFirstEmpty

def test_getFirstEmpty():
	column = [
		Token.EMPTY,
		Token.EMPTY,
		Token.EMPTY,
		Token.EMPTY,
		Token.YELLOW,
		Token.BLUE
	]
	assert getFirstEmpty(column) == 3

	column2 = [
		Token.EMPTY,
		Token.YELLOW,
		Token.BLUE,
		Token.YELLOW,
		Token.YELLOW,
		Token.BLUE
	]
	assert getFirstEmpty(column2) == 0

	column3 = [
		Token.BLUE,
		Token.YELLOW,
		Token.BLUE,
		Token.YELLOW,
		Token.YELLOW,
		Token.BLUE
	]
	assert getFirstEmpty(column3) == -1