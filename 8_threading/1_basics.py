#! /usr/bin/python3

from threading import Thread

COUNTER = 10

class ServerWorker(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		for i in range(COUNTER):
			print ("Server thread.")


class ClientWorker(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		for i in range(COUNTER):
			print ("Client thread.")

class Chat:
	def __init__(self):
		self.server = ServerWorker()
		self.client = ClientWorker()

	def start(self):
		self.server.start()
		self.client.start()

if __name__ == "__main__":
	chat = Chat()
	chat.start()
