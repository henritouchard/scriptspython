#this functions handle url requests

import requests

def urlRequest(url):
	
	#simulate requests as using a web browser to avoid forbiden Access
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	
	#request HTML code            
	try:
		#define header of the request to say it's not a bot and get HTML return
		response = requests.get(url, headers=headers)
	except requests.exceptions.RequestException as e:
		print ("WARNING : ", e)
		return False

	#condition if request was a success
	if (response.status_code == 200) :
		f = open('data.html', 'w')
		f.write(response.text)
		f.close()
		return True

	#status code give n° of error (404, 503...)
	print ("WARNING : failed to get data from url because of the following code : ", str(response.status_code))
	return False



	
