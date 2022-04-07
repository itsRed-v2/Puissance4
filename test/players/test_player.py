from p4.utils.color import Color
from p4.players.player import Player
from p4.utils.token import Token

def test_properties():
	player = Player(Token.YELLOW, Color.YELLOW + "JAUNE")
	assert player.token == Token.YELLOW
	assert player.displayName == Color.YELLOW + "JAUNE" + Color.RESET