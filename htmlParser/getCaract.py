import getInfo
import re

def colorvariationSaturn(soup):
	space = "           "
	value = "{"
	color = soup.find("div", class_="product-attributes__color-item")
	price = re.sub("[^0-9.]", "", color.next.next.text.replace(",", "."))
	color = color["data-value"]
	value += "\n"+ space +"  \"" + color + "\"" + ": " + price
	color = soup.find("div", class_="product-attributes__color-item product-attributes__color-item--active")
	price = re.sub("[^0-9.]", "", color.next.next.text.replace(",", "."))
	color = color["data-value"]
	value += "\n"+ space +"  \"" + color + "\"" + ": " + price + "\n"+space+"}"
	return '\"' + "price" + "\": " + value

def colorvariationAmazon(soup):
	colors = ["Noir", "Bleu", "Rouge", "Turquoise"]
	it = 0
	limit = 1
	space = "           "
	value = "{"
	while limit != None :
		limit = soup.find(id="color_name_"+str(it)+"_price")
		if limit != None :
			value += "\n"+ space +"  \"" + colors[it]\
			+ "\"" + ":" + getInfo.treat(limit.text)
		it += 1
	value += "\n"+ space +"}"
	return '\"' + "price" + "\": " + value

def getResellers(soup):
	sellers = soup.find("span", class_="bluetxt")
	if sellers != None :
		return sellers.text
	return ""
#seems need flash to get each reseller

#not used because of specificities :
# def getAvailability(status):
# 	if status != None :
# 		status = status.text
# 	else :
# 		status = "Unavailable"
# 	return jsonFormater.jsonFormater("availability", status)
