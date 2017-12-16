#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup

URL = "https://www.coinmarketcap.com/"

response = requests.get(URL)

if response.status_code == 200:
	data = BeautifulSoup(response.text, "html.parser")
	first_link = data.find("a", {"class": "currency-name-container"})

	print("First Crypto link: {}".format(first_link))

	print("All it's parents are:")
	for parent in first_link.parent:
		print(parent)
