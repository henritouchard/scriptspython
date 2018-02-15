#this functions handle html parsing

from bs4 import BeautifulSoup
import propertyGetter

def htmlParser(shop):
	if (shop == 0):
		propertyGetter.getSaturnProp()
	elif (shop == 1) :
		propertyGetter.getFnacProp()
	elif (shop == 2):
		propertyGetter.getAmazonProp()
	else:
		print("sorry shop is not reconized")
	#jsonFormater.jsonformat(table)