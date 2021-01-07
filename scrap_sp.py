import requests
import lxml.html as html
import os 
import datetime

name_p = 'LOGITECH'

HOME_URL = f'https://www.spdigital.cl/categories/search?q={name_p}&category_id=-1'
BASE_URL = 'https://www.spdigital.cl'
XPATH_HREF = '//div[@class="name"]/a/@href'


def parse_home():
	try:
		response = requests.get(HOME_URL)
		if response.status_code ==200:
			home = response.content.decode('utf-8')
			parsed = html.fromstring(home)
			links_to_products = parsed.xpath(XPATH_HREF)
			
			today = datetime.date.today().strftime('%d-%m-%y')
			if not os.path.isdir(today):
				os.mkdir(today)
			

			l = len(links_to_products)
			for i in range(l):
				links_to_products[i] = BASE_URL+links_to_products[i]
			print(links_to_products)	
			
			
				

	except ValueError as ve:
		print('error',ve)

def run():
	parse_home()

if __name__ == '__main__':
	run()





