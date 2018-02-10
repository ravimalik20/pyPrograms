#! /usr/bin/python3

from threading import Thread, Lock
from random import randint

NUM_WORKERS = 2

class Worker(Thread):
	l = []
	list_lock = Lock()

	def __init__(self, i):
		Thread.__init__(self)
		self.name = "Worker {}".format(i)

	def run(self):
		data = [self.name + ":" + str(randint(0, 100)) for i in range(10)]

		for d in data:
			# Acquire a lock
			Worker.list_lock.acquire()

			Worker.l.append(d)
			print ("{}: append to list: {}".format(self.name, d))

			# Release a lock
			Worker.list_lock.release()

		self.__show_list()

	def __show_list(self):
		Worker.list_lock.acquire()
		print ("{} : {}".format(self.name, Worker.l))
		Worker.list_lock.release()

if __name__ == "__main__":
	workers = [Worker(i) for i in range(NUM_WORKERS)]

	for worker in workers:
		worker.start()
