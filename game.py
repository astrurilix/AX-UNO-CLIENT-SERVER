from Cards import Card, cards
import random

class Game:

	def __init__(self, id):
		# Which player's turn is it? Initially player 1
		self.turn = 0
    	
    	# Are both players connected?
		self.ready = False

    	# game ID
		self.id = id

    	# deck
		self.deck = cards
		random.shuffle(self.deck)

    	# player 1 cards
		self.p1Cards = self.deck[0:7]

    	# player 2 cards
		self.p2Cards = self.deck[7:14]

    	# In UNO only the last move matters
		self.lastMove = self.deck[14]

    	# 7 distributed to each player + 1 on top of pile
		self.numCardsAssigned = 15 

    	# Two players
		self.wins = [0,0]

	def getLastMove(self):
		return self.lastMove

	def endTurn(self):
		self.turn = (self.turn + 1) % 2

	def play(self, player, move: Card):
		"""
		@Param: player- which player's move is this?

		No error checking in this function. Implement before.
		"""

		if move.ability != None:
			"""
			In case the move has an ability, the turn is retained. No need to switch turns.
			"""

			if move.ability == "d2":
				if player == 0:
					self.p2Cards.append(self.deck[self.numCardsAssigned])
					self.p2Cards.append(self.deck[self.numCardsAssigned + 1])

				else:
					self.p1Cards.append(self.deck[self.numCardsAssigned])
					self.p1Cards.append(self.deck[self.numCardsAssigned + 1])

				self.numCardsAssigned += 2

			# Other abilities simply retain the turn. No need for special checking

		else:
			self.turn = (player + 1) % 2

		try:
			if player == 0:
				index = self.findCard(move, player)
				if index != None: del self.p1Cards[index]
			else:
				index = self.findCard(move, player)
				if index != None: del self.p2Cards[index]

		except error as e:
			print("ran into error while playing move")

		self.lastMove = move
		

	def connected(self):
		return self.ready

	def findCard(self, card: Card, player):
		listOfCards = ""

		if player == 0:
			listOfCards = self.p1Cards
		else:
			listOfCards = self.p2Cards

		for index in range(0, len(listOfCards)):
			if listOfCards[index] == card:
				return index

		return None

	def draw(self, player):
		"""
		@Param: player- which player's move is this?

		No error checking in this function. Implement before.
		"""

		if player == 0:
			self.p1Cards.append(self.deck[self.numCardsAssigned])
		else:
			self.p2Cards.append(self.deck[self.numCardsAssigned])

		self.numCardsAssigned += 1
