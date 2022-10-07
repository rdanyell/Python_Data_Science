#!/usr/bin/env python3

import sys
import subprocess
import os

def main():
	if os.getenv("VIRTUAL_ENV") is None:
		print('You are not in the Virtual Environment')
	else: 
		envrn = os.getenv("VIRTUAL_ENV")
		if envrn.endswith('rdanyell02'):
			print("This is the right ex02 enviroment")
			os.system("pip3 install beautifulsoup4 PyTest")
			os.system("pip3 freeze > requirements.txt")
		else:
			print('Virtual Environment is different')


if __name__ == '__main__':
	main()

