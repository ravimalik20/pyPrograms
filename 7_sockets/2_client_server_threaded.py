from threading import Thread
from socket import socket, gethostname, AF_INET, SOCK_STREAM

class ServerWorker(Thread):
	def __init__(self):
		Thread.__init__(self)

		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.bind((gethostname(), 4567))

	def run(self):
		self.sock.listen()

		while True:
			print ("Server listening")
			(csock, add) = self.sock.accept()
			message = self.__receiveMessage(csock)

			print ("Message received: ", message)

			if message == "exit":
				print ("Server thread exiting.")
				break

	def __receiveMessage(self, sock):
		return sock.recv(1024).decode()

class ClientWorker(Thread):
	def __init__(self, message):
		Thread.__init__(self)

		self.message = message

	def run(self):
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((gethostname(), 4567))

		self.__sendMessage(sock, self.message)

		sock.close()

	def __sendMessage(self, sock, msg):
		sock.send(msg.encode("utf-8"))

server = ServerWorker()
server.start()

for i in range(5):
	c = ClientWorker("Client {}".format(i))
	c.start()

c = ClientWorker("exit")
c.start()
