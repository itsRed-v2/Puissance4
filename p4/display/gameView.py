import os

from p4.utils.color import Color
from p4.utils.token import Token

tokenColors = {
	Token.YELLOW: Color.YELLOW,
	Token.BLUE: Color.BLUE,
	Token.EMPTY: Color.GRAY
}

class View:
	def __init__(self, board):
		self.board = board
		self.footer = ""

	def displayBoard(self):
		
		line = "|" + Color.BOLD
		for i in range(self.board.WIDTH):
			line += str(i + 1).rjust(2, " ") + " "
		line += Color.RESET + "|"
		print(line)

		for row in range(self.board.HEIGHT):
			line = Color.RESET + "|"

			for col in range(self.board.WIDTH):
				line += Color.RESET

				token = self.board.getColumn(col)[row]
				line += tokenColors.get(token)
				
				lastToken = self.board.lastToken
				if (lastToken != None
						and lastToken.c == col
						and lastToken.r == row):
					line += Color.BOLD + " 0 "
				else: line += " O "
				
			line += Color.RESET + "|"
			
			print(line)

	def displayGame(self, playerName):
		header = f"C'est au tour du joueur {playerName}"
		permFooter = "Entrez \"help\" pour de l'aide"
		self.display(header, permFooter)
	
	def display_win(self, playerName):
		header = ""
		permFooter = f"Joueur {playerName} a gagné!"
		self.display(header, permFooter)
	
	def display(self, header, permFooter):
		print(Color.RESET)

		size = os.get_terminal_size()
		for i in range(size.lines - 6 - self.board.HEIGHT):
			print("")

		print(header + Color.RESET)

		self.displayBoard()

		print(self.footer + Color.RESET)
		print(permFooter)

		self.footer = ""