import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.prisonstudies.org')
prison_html = BeautifulSoup(r.text, 'html.parser')
def prisonA(my_html):
	for link in my_html.find_all('a'):
		if link.get('href') and '/country/' in link.get('href'):
			yield link.get('href')
			
def prisonDiv(my_html):
	for div in est_html.find_all('div'):
		if div.get('class') and "field-collection-item-field-number-of-establishments" in div.get('class'):
			return div.div.div.div.text
			
#continent_list = (prison(prison_html,'/map/'))
country_list = (prisonA(prison_html))
result_dict = {}
for i in country_list:
	country = i.split('/')[2]
	country_r = requests.get('http://www.prisonstudies.org'+i)
	est_html = BeautifulSoup(country_r.text, 'html.parser')
	est_num = prisonDiv(est_html).replace('\n',"")
	result_dict[country] = est_num
print(result_dict)