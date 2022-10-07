#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys
import time
import requests

def parse_info():
	time.sleep(5)
	print('Parsing finance.yahoo webpage')
	#Принимаем адрес и заголовки. Заголовки используются для того, чтобы клиент и сервер понимали, как интерпретировать данные, отправляемые и получаемые в запросе и ответе.
	
	# website = requests.get(f"https://finance.yahoo.com/quote/{sys.argv[1]}/financials", headers={'User-Agent' : 'Custom'})
	# OR
	# url = f'https://finance.yahoo.com/quote/{sys.argv[1]}/financials'
	# website = requests.get(url, headers={'User-Agent' : 'Custom user agent'})
	# OR
	url = f'https://finance.yaho.com/quote/{sys.argv[1]}/financials'
	headers={'User-Agent': 'Custom user agent'}
	try:
		website = requests.get(url, headers=headers)
		if website.status_code != 200:
			raise Exception
	except:
		print('Page is not found')
			# raise Exception
	else:
		print('~ Success ~\n')

		# Создаем BeautifulSoup объект, который принимает Текст с веб страницы.
		# Используем встроенный в Питон парсер built-in HTML parser
		soup = BeautifulSoup(website.text, 'html.parser')
		# print(soup)
		# Находим элементы по HTML атрибутам на странице. берем целую строку fin-row
		elements = soup.find_all('div', attrs={'data-test' : 'fin-row'})
		for i in elements:
			if i.find('div', attrs={'title' : sys.argv[2]}) is not None:
				cols = i.find_all('div', attrs={'data-test' : 'fin-col'})
				my_list = [col.text for col in cols]
				return tuple([sys.argv[2], *my_list]) # звездочка убирает квадратные скобки
		print("statement name is not found")
		exit(1)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Wrong num of arg')
		exit(1)
	
	try:
		info = parse_info()
		if info is None:
			raise Exception 
	except:	
		print('Invalid info')
	else:
		print(info)