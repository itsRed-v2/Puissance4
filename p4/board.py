from p4.utils.token import Token
from p4.utils.vector import Vector

from p4.functions import getFirstEmpty

class Board:
	def __init__(self, stringRows = None, height = 6, width = 7):
		self.columns = []
		self.lastToken = None
		self.HEIGHT = height
		self.WIDTH = width
		
		for c in range(self.WIDTH):
			column = []
			for l in range(self.HEIGHT):

				if stringRows != None:
					
					if stringRows[l][c] == 'O':
						column.append(Token.BLUE)
					elif stringRows[l][c] == 'X':
						column.append(Token.YELLOW)
					else: column.append(Token.EMPTY)

				else: column.append(Token.EMPTY)

			self.columns.append(column)
	
	def getColumn(self, index):
		if 0 <= index < self.WIDTH:
			return self.columns[index]

	def addToken(self, columnIndex, token):
		column = self.getColumn(columnIndex)
		if column == None: return None

		row = getFirstEmpty(column)
		if row != -1:
			column[row] = token
			self.lastToken = Vector(columnIndex, row)

		return row