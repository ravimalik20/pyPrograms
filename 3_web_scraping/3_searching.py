#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.coinmarketcap.com/"

response = requests.get(URL)

if response.status_code == 200:
	data = BeautifulSoup(response.text, "html.parser")

	# Searching using regex
	tags_starting_with_b = data.find_all(re.compile(r"^b"))
	for tag in tags_starting_with_b:
		print (tag.name)

	# Searching using a list of tags
	tags_in_list = data.find_all(["table", "ul", re.compile(r"^h")])
	for tag in tags_in_list:
		print (tag.name)

	# True. Find everything you can.
	tags_all = data.find_all(True)
	for tag in tags_all:
		print (tag.name)

	# Find using a custom function
	comp_func = lambda node: node.has_attr("class") and not node.has_attr("id")
	tags_func = data.find_all(comp_func)
	for tag in tags_func:
		print (tag.name)
