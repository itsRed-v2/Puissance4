import os

from p4.utils.color import Color
from p4.utils.token import Token

from p4.functions import tokenToString

class View:
	def __init__(self, board):
		self.board = board
		self.footer = ""

	def displayBoard(self):
		
		line = "|" + Color.BOLD
		for i in range(7):
			line += f" {i+1} "
		line += Color.RESET + "|"
		print(line)

		for row in range(6):
			line = Color.RESET + "|"

			for col in range(7):
				line += Color.RESET

				tokenID = self.board.getColumn(col)[row]
				match tokenID:
					case Token.BLUE:
						line += Color.BLUE
					case Token.YELLOW:
						line += Color.YELLOW
					case Token.EMPTY:
						line += Color.GRAY
				
				lastToken = self.board.lastToken
				if (lastToken != None
						and lastToken.c == col
						and lastToken.r == row):
					line += Color.BOLD + " 0 "
				else: line += " O "
				
			line += Color.RESET + "|"
			
			print(line)

	def displayGame(self, tourToken):
		print(Color.RESET)

		size = os.get_terminal_size()
		for i in range(size.lines - 12):
			print("")

		print(f"C'est au tour du joueur {tokenToString(tourToken)}")

		self.displayBoard()

		print(self.footer + Color.RESET)
		print("Entrez \"help\" pour de l'aide")

		self.footer = ""