#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
	data = BeautifulSoup(response.text, 'html.parser')
	crypto_list = data.find("table", {"id": "currencies"})

	# Exclude table header
	crypto_list.find("thead").decompose()

	crypto_list = crypto_list.find_all("tr")

	# Print crypto names
	for crypto in crypto_list:
		name = crypto.contents[3].find("a", {"class": "currency-name-container"})
		price = crypto.find("a", {"class": "price"})
		link = name.get("href")

		print ("{} : {} -> {}".format(name.text, price.text, link))
