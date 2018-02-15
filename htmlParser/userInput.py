
shopid = ["saturn", "fnac.com", "amazon"]

def getUserInput():
	url = input()
	return url

#checks if command is well formated
def checkUserInput(url):
	if (url == "exit"):
		return 1
	else :
		return url

def getShopId(url):
	it = 0
	for i in shopid :
		if (url.find(i) != -1) :
			break
		else :
			it += 1
	return it
