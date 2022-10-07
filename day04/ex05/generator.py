#!/usr/bin/env python3

import sys
import psutil

def generator():
	#использовать генератор
	try:
		with open(sys.argv[1]) as file:
			for line in file:
				yield line # ключевое слово, которое возвращает генератор
	except:
		print('Unable to open the file')

def main():
	for _ in generator():
		pass
	print(generator())
	mem = psutil.Process().memory_info().vms/(10**9) #переводит из наносекунд в секунды
	cpu = psutil.Process().cpu_times()
	print(f'Peak Memory Usage = {mem} Gb')
	print(f'User Time + System Time = {cpu.user + cpu.system}s')

if __name__ == '__main__':

    try:
        if len(sys.argv) != 2:
	        raise Exception
        main()
    except BaseException:
	    print("ERROR")

#pip3 install psutil in venv
