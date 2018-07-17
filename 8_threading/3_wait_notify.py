from threading import Thread, Condition

glock = Condition()

class ConsumerThread(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		with glock:
			print ("Consumer thread.")
			glock.notify_all()

class ProducerThread(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		with glock:
			print ("Lock acquired. Dispatching threads and waiting.")

			ct = ConsumerThread()
			ct.start()
			glock.wait()

			print ("Notified.")

pt = ProducerThread()
pt.start()


