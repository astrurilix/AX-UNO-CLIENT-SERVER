class Card:
	# Game card. 

	def __init__(self, number, color, ability, wild):
		# Number on the face of the card
		self.number  = number
		# Which color is the thing
		self.color   = color
		# Draw 2 / Reverse etc
		self.ability = ability
		# Wild card?
		self.wild = wild

	def __eq__(self, other):

		return (self.number == other.number) and (self.color == other.color) and (self.ability == other.ability) and (self.wild == other.wild)

cards = [
	# Red Cards
	Card(0, (255, 0, 0), None, None),
	Card(1, (255, 0, 0), None, None),
	Card(2, (255, 0, 0), None, None),
	Card(3, (255, 0, 0), None, None),
	Card(4, (255, 0, 0), None, None),
	Card(5, (255, 0, 0), None, None),
	Card(6, (255, 0, 0), None, None),
	Card(7, (255, 0, 0), None, None),
	Card(8, (255, 0, 0), None, None),
	Card(9, (255, 0, 0), None, None),
	Card(1, (255, 0, 0), None, None),
	Card(2, (255, 0, 0), None, None),
	Card(3, (255, 0, 0), None, None),
	Card(4, (255, 0, 0), None, None),
	Card(5, (255, 0, 0), None, None),
	Card(6, (255, 0, 0), None, None),
	Card(7, (255, 0, 0), None, None),
	Card(8, (255, 0, 0), None, None),
	Card(9, (255, 0, 0), None, None),
	# Ability cards
	Card("d2", (255, 0, 0), "d2", None),
	Card("d2", (255, 0, 0), "d2", None),
	Card("skip", (255, 0, 0), "skip", None),
	Card("skip", (255, 0, 0), "skip", None),
	Card("rev", (255, 0, 0), "rev", None),
	Card("rev", (255, 0, 0), "rev", None),

	# Green Cards
	Card(0, (0, 255, 0), None, None),
	Card(1, (0, 255, 0), None, None),
	Card(2, (0, 255, 0), None, None),
	Card(3, (0, 255, 0), None, None),
	Card(4, (0, 255, 0), None, None),
	Card(5, (0, 255, 0), None, None),
	Card(6, (0, 255, 0), None, None),
	Card(7, (0, 255, 0), None, None),
	Card(8, (0, 255, 0), None, None),
	Card(9, (0, 255, 0), None, None),
	Card(1, (0, 255, 0), None, None),
	Card(2, (0, 255, 0), None, None),
	Card(3, (0, 255, 0), None, None),
	Card(4, (0, 255, 0), None, None),
	Card(5, (0, 255, 0), None, None),
	Card(6, (0, 255, 0), None, None),
	Card(7, (0, 255, 0), None, None),
	Card(8, (0, 255, 0), None, None),
	Card(9, (0, 255, 0), None, None),
	# Ability Cards
	Card("d2", (0, 255, 0), "d2", None),
	Card("d2", (0, 255, 0), "d2", None),
	Card("skip", (0, 255, 0), "skip", None),
	Card("skip", (0, 255, 0), "skip", None),
	Card("rev", (0, 255, 0), "rev", None),
	Card("rev", (0, 255, 0), "rev", None),

	# Blue Cards
	Card(0, (0, 0, 255), None, None),
	Card(1, (0, 0, 255), None, None),
	Card(2, (0, 0, 255), None, None),
	Card(3, (0, 0, 255), None, None),
	Card(4, (0, 0, 255), None, None),
	Card(5, (0, 0, 255), None, None),
	Card(6, (0, 0, 255), None, None),
	Card(7, (0, 0, 255), None, None),
	Card(8, (0, 0, 255), None, None),
	Card(9, (0, 0, 255), None, None),
	Card(1, (0, 0, 255), None, None),
	Card(2, (0, 0, 255), None, None),
	Card(3, (0, 0, 255), None, None),
	Card(4, (0, 0, 255), None, None),
	Card(5, (0, 0, 255), None, None),
	Card(6, (0, 0, 255), None, None),
	Card(7, (0, 0, 255), None, None),
	Card(8, (0, 0, 255), None, None),
	Card(9, (0, 0, 255), None, None),
	# Ability Cards
	Card("d2", (0, 0, 255), "d2", None),
	Card("d2", (0, 0, 255), "d2", None),
	Card("skip", (0, 0, 255), "skip", None),
	Card("skip", (0, 0, 255), "skip", None),
	Card("rev", (0, 0, 255), "rev", None),
	Card("rev", (0, 0, 255), "rev", None),

	# Yellow Cards
	Card(0, (250, 192, 32), None, None),
	Card(1, (250, 192, 32), None, None),
	Card(2, (250, 192, 32), None, None),
	Card(3, (250, 192, 32), None, None),
	Card(4, (250, 192, 32), None, None),
	Card(5, (250, 192, 32), None, None),
	Card(6, (250, 192, 32), None, None),
	Card(7, (250, 192, 32), None, None),
	Card(8, (250, 192, 32), None, None),
	Card(9, (250, 192, 32), None, None),
	Card(1, (250, 192, 32), None, None),
	Card(2, (250, 192, 32), None, None),
	Card(3, (250, 192, 32), None, None),
	Card(4, (250, 192, 32), None, None),
	Card(5, (250, 192, 32), None, None),
	Card(6, (250, 192, 32), None, None),
	Card(7, (250, 192, 32), None, None),
	Card(8, (250, 192, 32), None, None),
	Card(9, (250, 192, 32), None, None),
	# Ability Cards
	Card("d2", (250, 192, 32), "d2", None),
	Card("d2", (250, 192, 32), "d2", None),
	Card("skip", (250, 192, 32), "skip", None),
	Card("skip", (250, 192, 32), "skip", None),
	Card("rev", (250, 192, 32), "rev", None),
	Card("rev", (250, 192, 32), "rev", None),
	
    # Wild Cards
    Card("cc", (0, 0, 0), None, "cc"),
    Card("cc", (0, 0, 0), None, "cc"),
    Card("cc", (0, 0, 0), None, "cc"),
    Card("cc", (0, 0, 0), None, "cc"),
    Card("p4", (0, 0, 0), None, "p4"),
    Card("p4", (0, 0, 0), None, "p4"),
    Card("p4", (0, 0, 0), None, "p4"),
    Card("p4", (0, 0, 0), None, "p4"),
]

wilds = [
    Card("p4", (255, 0, 0), None, None),
    Card("cc", (255, 0, 0), None, None),
    Card("p4", (0, 255, 0), None, None),
    Card("cc", (0, 255, 0), None, None),
    Card("p4", (0, 0, 255), None, None),
    Card("cc", (0, 0, 255), None, None),
    Card("p4", (250, 192, 32), None, None),
    Card("cc", (250, 192, 32), None, None),

]