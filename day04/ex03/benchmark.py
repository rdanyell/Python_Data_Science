#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

def lloop():
	sum_square = 0
	for i in range(1, n + 1):
		sum_square += i * i
		return sum_square

def reduce():
	sum_square = reduce(lambda y, x: y + x**2, range(1, n + 1))
	return sum_square


def my_time(func_name, n):
	times = timeit.timeit(lambda: func_name, number = n)
	return times
	
if __name__ == '__main__':
	
	try:
		if len(sys.argv) != 4:
			raise Exception ("Wrong number of args")
		number = int(sys.argv[2])
		n = int(sys.argv[3])

		if sys.argv[1] == 'loop':
			arg = lloop
		elif sys.argv[1] == 'reduce':
			arg = reduce
		time_arg = my_time(arg, n)
	except Exception as err:
		print("Error!")
		print(err)
	else:
		print(time_arg)

	#./benchmark.py reduce 100 10
	#./benchmark.py loop 100 10
