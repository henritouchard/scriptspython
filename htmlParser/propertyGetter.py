import jsonFormater
from bs4 import BeautifulSoup
import re
import getInfo
import getCaract

def openFile():
	f = open("data.html", 'r')
	soup = BeautifulSoup(f.read(), 'html.parser')
	return soup


def getSaturnProp():
	InfoList = []

	soup = openFile()

	name = getInfo.getValueByItem(soup, "name", 2, "name")
	InfoList.append(name)

	is_color = soup.find("div", class_="product-attributes__color-item")
	if is_color != None :
		price = getCaract.colorvariationSaturn(soup)
	else :
		price = getInfo.getValueByItem(soup, "price", 1, "price")
	InfoList.append(price)
	
	oldprice = getInfo.getInfoClass(soup, "div", "old-price-block")
	if oldprice != None :
		oldprice = getInfo.treat(oldprice.next.next.text)
		oldprice = re.sub("[^0-9],", "", oldprice)
		oldprice = jsonFormater.jsonFormater("older price", float(oldprice))
	else :
		oldprice = jsonFormater.jsonFormater("older price", "no older price")
	InfoList.append(oldprice)

	devise = getInfo.getInfoItemprop(soup, "priceCurrency", "content")
	devise = jsonFormater.jsonFormater("devise", devise)
	InfoList.append(devise)

	availability = getInfo.getInfoClass(soup, "span", "snk_avail_clr01 snk_tick snk_bold")
	if availability != None :
		availability = 1
	else :
		availability = 5
	availability = jsonFormater.jsonFormater("availability", availability)
	InfoList.append(availability)

	comment_numb = getInfo.getValueByItem(soup, "reviewCount", 0, "comment number")
	InfoList.append(comment_numb)

	rate = getInfo.getValueByItem(soup, "ratingValue", 1, "rate")
	InfoList.append(rate)

	resellers = jsonFormater.jsonFormater("resellers", "")
	InfoList.append (resellers)

	jsonFormater.jsonResult(InfoList)



def getFnacProp():

	InfoList = []

	soup = openFile()

	name = getInfo.getValueByItem(soup, "name", 2, "name")
	InfoList.append(name)

	price = getInfo.getValueByClass(soup, "strong", "product-price", 1, "price")
	InfoList.append (price)

	oldprice = getInfo.getOldprice(soup, "del", "oldPrice")
	InfoList.append (oldprice)

	devise = getInfo.getInfoItemprop(soup, "priceCurrency", "content")
	devise = jsonFormater.jsonFormater("devise", devise)
	InfoList.append (devise)

	availability = soup.find("p", class_="ProductSellers-unavailable-text")
	if availability != None :
		if re.search("Indisponible", availability.text):
			availability = 5
		else :
			availability = 1
		availability = jsonFormater.jsonFormater("availability", availability)
	else :
		availability = 1
		availability = jsonFormater.jsonFormater("availability", availability)
	InfoList.append(availability)
	
	comment_numb = getInfo.getInfoItemprop(soup, "ratingCount", "content")
	if comment_numb != "None" :
		comment_numb = re.sub("[^0-9]", "", comment_numb)
		comment_numb = jsonFormater.jsonFormater("comment number", int(comment_numb))
	else :
		comment_numb = jsonFormater.jsonFormater("comment number", comment_numb)
	InfoList.append (comment_numb)	

	rate = getInfo.getInfoItemprop(soup, "ratingValue", "content")
	if rate != "None" :
		rate = jsonFormater.jsonFormater("rate", float(rate))
	else :
		rate = jsonFormater.jsonFormater("rate", rate)
	InfoList.append (rate)

	resellers = soup.find_all("a", class_="ProductSellers-tabControl To-anchor js-omniture-action")
	if len(resellers) > 1 and resellers[1]["data-omniture-action"] == "MpBrandOffer":
		resellers = getCaract.getResellers(soup)
		resellers = jsonFormater.jsonFormater("resellers", resellers)
	else :
		resellers = jsonFormater.jsonFormater("resellers", "")
	InfoList.append (resellers)	
	jsonFormater.jsonResult(InfoList)



def getAmazonProp():
	InfoList = []
	
	soup = openFile()

	name = getInfo.getInfoById(soup, "productTitle")
	name = jsonFormater.jsonFormater("name", name)
	InfoList.append (name)

	is_color = soup.find(id ="variation_color_name")
	if is_color != None :
		price = getCaract.colorvariationAmazon(soup)
	else :
		price = getInfo.getInfoById(soup, "priceblock_ourprice")
		if price != "None" :
			price = getInfo.treat(price.string)
			price = jsonFormater.jsonFormater("price", float(price))
		else :
			price = "Exception"
	InfoList.append (price)

	oldprice = soup.find("span", class_="a-text-strike")
	if oldprice != None:
		oldprice = jsonFormater.jsonFormater("old price", float(getInfo.treat(oldprice.text)))
	else :
		oldprice = jsonFormater.jsonFormater("old price", "no older price")
	InfoList.append (oldprice)

	devise = getInfo.getInfoById(soup, "priceblock_ourprice")
	devise = re.sub("[^A-Z]", "", devise)
	devise = jsonFormater.jsonFormater("devise", devise)
	InfoList.append (devise)

	availability = getInfo.getInfoClass(soup, "span", "a-size-medium a-color-success")
	if availability != None :
		if re.search("plus que", availability.text):
			availability = 2
		elif re.search("rupture", availability.text) or re.search("bientôt", availability.text):
			availability = 5
		else :
			availability = 1
	else :
		availability = "None"
	availability = jsonFormater.jsonFormater("availability", availability)
	InfoList.append(availability)

	comment_numb = soup.find(id="acrCustomerReviewText")
	if comment_numb != None :
		comment_numb = re.sub("[^0-9]", "", comment_numb.string)
		comment_numb = jsonFormater.jsonFormater("comment number", int(comment_numb))
	else :
		comment_numb = jsonFormater.jsonFormater("comment number", "None")
	InfoList.append (comment_numb)

	rate = soup.find("i", class_="a-icon a-icon-star a-star-4-5")
	if rate != None :
		rate = re.sub("[^0-9.].", "", rate.next.text)
		rate = jsonFormater.jsonFormater("rate", float(rate))
	else :
		rate = jsonFormater.jsonFormater("rate", "None")
	InfoList.append (rate)

	resellers = jsonFormater.jsonFormater("resellers", "")
	InfoList.append (resellers)		
	jsonFormater.jsonResult(InfoList)
