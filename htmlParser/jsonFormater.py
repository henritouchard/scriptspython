
def jsonFormater(title, car):
	if (isinstance(car, str)):
		prop = '\"' + title + "\": " + '\"' + car.strip() + '\"'
	elif (isinstance(car, float) or isinstance(car, int)):
		prop = '\"' + title + "\": "+ str(car)
	return prop


def jsonResult(tab):
	print ('{')
	for i in tab :
		print("  " + i)
	print('}')

def colorvariation(soup):
	colors = ["Noir", "Bleu", "Rouge", "Turquoise"]
	it = 0
	limit = 1
	space = "           "
	value = "{"
	while limit != None :
		limit = soup.find(id="color_name_"+str(it)+"_price")
		if limit != None :
			value += "\n"+ space +"  \"" + colors[it]\
			+ "\"" + ":" + getinfo.treat(limit.text)
		it += 1
	value += "\n"+ space +"}"
	return '\"' + "price" + "\": " + value