import jsonFormater
import re

def treat(price):
	price = price.replace("€", ".")
	price = price.replace(",", ".")
	#à voir pour les assembler
	price = re.sub("[^0-9.]", "", price)
	if (price.endswith('.')):
		price = price + "00"
	return price

def getInfoClass(soup, balise, name): 
	return soup.find(balise, class_=name)

def getInfoItemprop(soup, balise, search):
	info = soup.find(itemprop=balise)
	if info != None :
		return info[search]
	else :
		return "None"

def getInfoById(soup, id):
	info = soup.find(id=id)
	if info != None:
		return info.string
	else:
		return "None"

def getOldprice(soup, balisetype, balname):
	old = soup.find(balisetype, class_=balname)
	if old != None and old != "":
		old = old.text
		old = treat(old)
		old = jsonFormater.jsonFormater("old price", float(old))
	else :
		old = jsonFormater.jsonFormater("old price", "no older price")
	return old

def getValueByClass(soup, balise, classname, type, name):
	val = soup.find(balise, class_=classname)
	if val != None :
		val = val.text
		if type == 0 :
			val = int(treat(val))
		elif type == 1 :
			val = float(treat(val))
	else :
		val = "None"
	val = jsonFormater.jsonFormater(name, val)
	return val

def getValueByItem(soup, balise, type, name):
	val = soup.find(itemprop=balise)
	if val != None :
		val = val.text
		if type == 0 :
			val = int(treat(val))
		elif type == 1 :
			val = float(treat(val))
	else:
		val = "None"
	val = jsonFormater.jsonFormater(name, val)
	return val


