"""
server.py
Server for AX-UNO
"""

# Importing Nexessary Modules
import socket
import sys
import pickle

from _thread import *
from game import Game # Game Logic Goes Here
from multiprocessing.connection import Listener

"""
SERVER CONFIGURATION

When started, this will read server_connection.txt file
and get the network needed to start the server.

| Current Network Configuration:
| IP	 : 10.41.3.165
| PORT : 7723

"""
with open('server_connection.txt') as f:
    contents = f.read()

ip, port = contents.split("\n")

_, ip = ip.split(":")
_, port = port.split(":")

port = int(port)

# Starting Connection
s = Listener((ip, port))
print("Waiting for a connection, Server Started")

"""
GAME INITIALIZATION

Initialize some variables.
-> Connected : Keep Track of Connected Client
-> Games	 : Dictionary to store game instances
-> idCount	 : Client Counter

"""
connected = set()
games = dict()
idCount = 0

"""
CLIENT THREAD FUNCTION

Handle Communication with a client, 
send the player ID to client,
Enters a loop where it waits for data from client.

It will update the game states; send the game state
to client or end the game
"""

def client_thread(conn, p, gameId, games):

	global idCount
	conn.send(p) # send player number. No pickling needed
	print("sending id")

	reply = ""
	# User can either send a move, or inform that they've drawn a card. 

	while True:

		"""
   		DATA RECEPTION
      
		The server tries to receive data from client
		if it fails, it will print an error message and break the loop.
      	"""
		try:
			data = conn.recv()
			print(data)
   
			"""
   			GAME EXISTENCE CHECK

			Server will check if a gameid is
			avalaiable in games dictionary.

			If not, it will print message and 
    		  break the loop
      		"""
			if gameId in games:
				# Get game for this player
				game = games[gameId]
				
				"""
				DATA PROCESSING
				
				If server received data, it will process it
				"""

				if not data:
					print("No data received")
					break

				else:
					"""
     				> GET
					Send current game state back to the client

         			"""
					if data == "get":
						reply = game
						conn.send(reply)
					"""
     				> MOVE
					Receives the next message from client
					Call play method of the game object
					Update the games in games dictionary
					Send the updated game state back to client

         			"""
					if data == "move":
						newMove = conn.recv()

						# This is a move
						move = newMove

						# Move will be of type Class
						game.play(p, move)

						games[gameId] = game
						reply = game
						conn.send(reply)
					"""
     				> DRAW
					Calls Draw method of game object
     				Update game in game dictionary
					Send updated game state back to client

         			"""
					if data == "draw":
						game.draw(p)

						games[gameId] = game
						reply = game
						conn.send(reply)
					
					if data == "crp4":
						reply = game.changeCardColor('p4', 'red')
						conn.send(reply)
					if data == "crcc":
						reply = game.changeCardColor('cc', 'red')
						conn.send(reply)
					
					if data == "cgp4":
						reply = game.changeCardColor('p4', 'green')
						conn.send(reply)
					if data == "cgcc":
						reply = game.changeCardColor('cc', 'green')
						conn.send(reply)
					
					if data == "cbp4":
						reply = game.changeCardColor('p4', 'blue')
						conn.send(reply)
					if data == "cbcc":
						reply = game.changeCardColor('cc', 'blue')
						conn.send(reply)
					
					if data == "cyp4":
						reply = game.changeCardColor('p4', 'yellow')
						conn.send(reply)
					if data == "cycc":
						reply = game.changeCardColor('cc', 'yellow')
						conn.send(reply)
						
					"""
     				> END
					Calls endTurn method of Game object
					Update game in game dictionary
					Send updated game state back to client

         			"""
					if data == "end":
						game.endTurn()
						games[gameId] = game

						conn.send(game)

			else:
				print("No game ID found.")
				break

		except:
			print("error")
			break
	"""
	GAME DELETION
 
	After the loop, server tries to delete game from games dictionary
	If it fails, it passes
 
	"""
	try:
		del games[gameId]
	except:
		pass
	idCount -= 1
	conn.close()

"""
CLIENT DISCONNECTION

Server Decrement idCount and Closes the connection with client

"""
while True:
	conn = s.accept()

	idCount += 1

	p = 0
	gameId = (idCount - 1)//2

	if idCount % 2 == 1:
		games[gameId] = Game(gameId)
	else:
		games[gameId].ready = True
		p = 1

	start_new_thread(client_thread, (conn, p, gameId, games))
