#!/usr/bin/python3.3
# coding: utf8

import sys
import os
import myRequester
import htmlParser
import userInput
from bs4 import BeautifulSoup

# http://www.saturn.de/de/product/_withings-wbs-04-body-cardio-2147129.html
# http://www.fnac.com/Enceinte-Bluetooth-JBL-Charge-2-Bleu-Outdoor/a8758271/w-4
# https://www.amazon.fr/JBL-Charge-Bluetooth-Résistante-Projections/dp/B00XPTRF0Q
#gets user command
		
#url entered by user
url = None
#shop id determine what shop is asked by user
shop_id = None

print ("Please enter a url to get informations: ")
#main loop
while (1):
	url = userInput.getUserInput()
	status = userInput.checkUserInput(url)
	if (status == 1):
		print ("Exiting...")
		os.remove("data.html")
		sys.exit(0)
	if myRequester.urlRequest(url) == True :
		shop_id = userInput.getShopId(url)
		htmlParser.htmlParser(shop_id)
	else :
		print ("Usage : type url to get info from product. You can type exit to exit and clean repo")




	

