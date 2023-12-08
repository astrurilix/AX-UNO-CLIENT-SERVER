from Cards import Card, cards, wilds
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
		self.p1Cards = self.deck[0:3]

    	# player 2 cards
		self.p2Cards = self.deck[4:7]

    	# In UNO only the last move matters
		self.lastMove = self.deck[8]

    	# 7 distributed to each player + 1 on top of pile
		self.numCardsAssigned = 9
    	# # player 1 cards
		# self.p1Cards = self.deck[0:7]

    	# # player 2 cards
		# self.p2Cards = self.deck[7:14]

    	# # In UNO only the last move matters
		# self.lastMove = self.deck[14]

    	# # 7 distributed to each player + 1 on top of pile
		# self.numCardsAssigned = 15 

    	# Two players
		self.wins = [0,0]

		# Get Wild Card IDs
		self.p4Red  = wilds[0]
		self.ccRed = wilds[1]
		self.p4Green = wilds[2]
		self.ccGreen = wilds[3]
		self.p4Blue = wilds[4]
		self.ccBlue = wilds[5]
		self.p4Yellow = wilds[6]
		self.ccYellow = wilds[7]

		self.resetTimer = 0

	def getLastMove(self):
		return self.lastMove

	def getP1Cards(self):
		return self.p1Cards
	
	def getP2Cards(self):
		return self.p2Cards
	
	def endTurn(self):
		self.turn = (self.turn + 1) % 2

	def check_winner(self):
		if len(self.p1Cards) == 0:
			self.wins[0] += 1
			return 0 # Player 1 wins
		elif len(self.p2Cards) == 0:
			self.wins[1] += 1
			return 1 # Player 2 wins
		else:
			return None # No winner yet	
			
	def setWinner(self):
		self.wins[0] += 1

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
		elif move.wild != None:
			if move.wild == "p4":
				if player == 0:
					self.p2Cards.append(self.deck[self.numCardsAssigned])
					self.p2Cards.append(self.deck[self.numCardsAssigned + 1])
					self.p2Cards.append(self.deck[self.numCardsAssigned + 2])
					self.p2Cards.append(self.deck[self.numCardsAssigned + 3])

				else:
					self.p1Cards.append(self.deck[self.numCardsAssigned])
					self.p1Cards.append(self.deck[self.numCardsAssigned + 1])
					self.p1Cards.append(self.deck[self.numCardsAssigned + 2])
					self.p1Cards.append(self.deck[self.numCardsAssigned + 3])
				
				self.numCardsAssigned += 4
    
				self.turn = (player) % 2
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

		# Check for a winner after each move 
		winner = self.check_winner()
		if winner is not None:
			self.reset() # Reset the game if there is a winner
			return
	
	def uno_fail(self, player):
		if player == 0:
			self.p1Cards.append(self.deck[self.numCardsAssigned])
			self.p1Cards.append(self.deck[self.numCardsAssigned + 1])
			self.numCardsAssigned +=2
		else:
			self.p2Cards.append(self.deck[self.numCardsAssigned])
			self.p2Cards.append(self.deck[self.numCardsAssigned + 1])
			self.numCardsAssigned +=2
		
	def changeCardColor(self, type, color):
		# Split into Type
		result = None
		if type=="cc":
			if color == "red":
				result = self.ccRed
			if color == "green":
				result = self.ccGreen
			if color == "blue":
				result = self.ccBlue
			if color == "yellow":
				result = self.ccYellow
		if type=="p4":
			if color == "red":
				result = self.p4Red
			if color == "green":
				result = self.p4Green
			if color == "blue":
				result = self.p4Blue
			if color == "yellow":
				result = self.p4Yellow
		self.lastMove = result
		return result
	

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
	
	def reset(self):
		if self.resetTimer == 25:
			self.turn = 0 
			self.ready = True
			self.deck = cards
			random.shuffle(self.deck)
			self.p1Cards = self.deck[0:7]
			self.p2Cards = self.deck[7:14]
			self.lastMove = self.deck[14]
			self.numCardsAssigned = 15
			self.resetTimer = 0
		else :
			self.resetTimer += 1
		print("reset")

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