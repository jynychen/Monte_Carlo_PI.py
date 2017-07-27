from random import random

N = 100000

def fn1():
	pi = 4.0 * len([1 for i in range(N)  if random() ** 2 + random() ** 2 < 1]) / N
	return pi

def fn2():
	C = 0
	for i in range(N):
		if random() ** 2 + random() ** 2 < 1:
			C += 1
	pi = 4.0 * C / N
	return pi

print(fn1(), fn2())