from threading import Timer

def hello():
	print ("Hello world.")

def helloWithDelay(n):
	print ("Printing hello with a delay of {} seconds.".format(n))

	t = Timer(n, hello)
	t.start()

hello()
helloWithDelay(4)
