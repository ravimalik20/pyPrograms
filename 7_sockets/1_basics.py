#! /usr/bin/python3

import socket

# Creating a socket

# AF_INET = IPv4, SOCK_STREAM = tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
s.close()

# Server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 2500))
# 5 means queue up at max 5 requests
server.listen(5)
server.close()
