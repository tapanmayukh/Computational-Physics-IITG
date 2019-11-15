import random


def f(arr, x):
	n = len(arr)
	
	val = 0.0
	for i in range(n):
		val += arr[i] * pow(x, n - 1 - i)
	
	return val


def bisect(arr, a, b):
	if f(arr, a) == 0:
		return a
	if f(arr, b) == 0:
		return b
	
	if f(arr, a) * f(arr, b) > 0:
#		print("Points lie on the same side of x-axis")
		return
	
	tol = pow(10, -5)
	while True:
		mid = (a + b) / 2.0
		
		if abs(f(arr, mid)) < tol:
			return mid
		
		if f(arr, a) * f(arr, mid) < 0:
			b = mid
		else:
			a = mid

def derivate(func, arr, val):
	h = pow(10, -9)
	d = (func(arr, val + h) - func(arr, val)) / h
	
	return d


if __name__ == "__main__":
	arr = [1, 0, 0, 0, 0, -1, -1]
	a, b = -10, 0
	
#	while f(arr, a) * f(arr, b) > 0:
#		a = random.randrange(-100, 101)
#		b = random.randrange(-100, 101)

	z = bisect(arr, a, b)
	d = derivate(f, arr, z)
	print("Zero:", z)
	print("Derivative at x = {}: {}".format(z, d))
