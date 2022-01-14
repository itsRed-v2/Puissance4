import os

from p4.utils.color import Color
from p4.utils.token import Token

from p4.functions import tokenToString

def displayBoard(board):
	
	line = "|" + Color.BOLD
	for i in range(7):
		line += f" {i+1} "
	line += Color.RESET + "|"
	print(line)

	for row in range(6):
		line = Color.RESET + "|"

		for col in range(7):
			line += Color.RESET

			tokenID = board.getColumn(col)[row]
			if tokenID == Token.BLUE:
				line += Color.BLUE
			elif tokenID == Token.YELLOW:
				line += Color.YELLOW
			else: line += Color.GRAY

			line += " O "
			
		line += Color.RESET + "|"
		
		print(line)

def displayGame(board, footer, tourToken):
	print(Color.RESET)

	size = os.get_terminal_size()
	for i in range(size.lines - 12):
		print("")

	print(f"C'est au tour du joueur {tokenToString(tourToken)}")

	displayBoard(board)

	print(footer + Color.RESET)
	print("Entrez \"help\" pour de l'aide")