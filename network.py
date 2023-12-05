import socket
from multiprocessing.connection import Client

class Network:

	"""
	INITIALIZATION
	
	Called when an instance of Network Class is created
	Initiate Server IP Address, Port, and Client Object
	Calls Connect method toconnect to server and get player method
 
	"""
	def __init__(self):
		# self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = '10.42.0.107'
		self.port = 7723
		self.client = Client((self.server, self.port))
		self.addr = (self.server, self.port)
		# which player number are we?
		self.playerNumber = self.connect()
	"""
	GET PLAYER NUMBER
  
	Returns the player number received from server
	if fails, print error message
  
	"""
	def getPlayerNumber(self):
		return self.playerNumber

	"""
	CONNECT
 
	Connect to Server and returns player number received
	If fails, print error message
	
 	"""
	def connect(self):
		try: 
			# self.client.connect(self.addr)
			return self.client.recv()
		except socket.error as e:
			str(e)
			print("Could not connect")
	"""
	SEND
 
	Send data to server
	There are 2 type of daya, C and M
	
	> C : Command
	Send command to server and returns the response
	
	> M : Move
 	Doesn't return immediately because it expects send
	Card object next
	Send move to server and returns the response, if fails
	print error message
 
 	"""
	def send(self, data, typeOfData):
		"""
		Param: type- What type of data are you sending? "C" for command or "M" for move
		"""

		if typeOfData == "C":
			# Sending a command and not a move
			try: 
				self.client.send(data)

				# When the command is move, we have to send the Card object as well. 
				# Don't return immediately.
				if data != "move":
					receivedData = self.client.recv()
					return receivedData

			except socket.error as e:
				print(e)

		elif typeOfData == "M":
			# Sending a move and not a command
			try:
				self.client.send(data)
				receivedData = self.client.recv()
				return receivedData

			except socket.error as e:
				print(e)