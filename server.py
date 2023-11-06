import socket
import sys
import pickle
# Main Packages

from _thread import *
from game import Game
from multiprocessing.connection import Listener

# Getting Connection Information
with open('connection.txt') as f:
    contents = f.read()

ip, port = contents.split("\n")

_, ip = ip.split(":")       # 192.168.1.170
_, port = port.split(":")   # 7723

port = int(port)

# Starting Connection
s = Listener((ip, port))
print("Waiting for a connection, Server Started")

# Game initialization
connected = set()
games = dict()
idCount = 0

def client_thread(conn, p, gameId, games):

	global idCount
	conn.send(p) # send player number. No pickling needed
	print("sending id")

	reply = ""
	# User can either send a move, or inform that they've drawn a card. 

	while True:

		try:
			data = conn.recv()
			print(data)

			if gameId in games:
				# Get game for this player
				game = games[gameId]

				if not data:
					print("No data received")
					break

				else:

					if data == "get":
						reply = game
						conn.send(reply)

					if data == "move":
						newMove = conn.recv()

						# This is a move
						move = newMove

						# Move will be of type Class
						game.play(p, move)

						games[gameId] = game
						reply = game
						conn.send(reply)

					if data == "draw":
						game.draw(p)

						games[gameId] = game
						reply = game
						conn.send(reply)

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

	try:
		del games[gameId]
	except:
		pass
	idCount -= 1
	conn.close()


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
