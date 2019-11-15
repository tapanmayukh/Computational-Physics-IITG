from math import sqrt, ceil


def strum(pol, A):
	if len(pol) >= len(A) + 1:
		return
	
	pol.append([1])
	pol.append([1, -A[0][0]])
	
	for i in range(2, len(A) + 1):
		pol.append([0 for _ in range(i + 1)])
		for j in range(i + 1):
			if j == 0:
				pol[i][j] = 1
			elif j < i:
				pol[i][j] = pol[i-1][j] - A[i-1][i-1] * pol[i-1][j-1]
			else:
				pol[i][j] = - A[i-1][i-1] * pol[i-1][j-1]
		
		for j in range(2, i + 1):
			pol[i][j] -= A[i-1][i-2] * A[i-1][i-2] * pol[i-2][j - 2]


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
	
	tol = pow(10, -5)
	while True:
		mid = (a + b) / 2.0
		
		if abs(f(arr, mid)) < tol:
			return mid
		
		if f(arr, a) * f(arr, mid) < 0:
			b = mid
		else:
			a = mid


def find_zeros(pol, interval):
	interval.insert(1, -pol[1][1])
	
	for i in range(2, len(pol)):
		zeros = []
		for j in range(len(interval) - 1):
			z = bisect(pol[i], interval[j], interval[j+1])
			zeros.append(z)
		
		if i != len(pol) - 1:
			del interval[1:-1]
			
			for i in range(len(zeros)):
				interval.insert(-1, zeros[i])
	
	return zeros


if __name__ == "__main__":
#	A = [[1, sqrt(6), 0], [sqrt(6), 3, -sqrt(2)], [0, -sqrt(2), 1]]
	A = [[4, 3, 0], [3, 1, -1], [0, -1, 1]]
	
	max_l = 0
	for i in range(len(A)):
		temp = sum([abs(x) for x in A[i]])
		if max_l < ceil(temp):
			max_l = ceil(temp)
	
	interval = [-max_l, max_l]
	
	pol = []
	strum(pol, A)
	
	zeros = find_zeros(pol, interval)
	
	print("Eigenvalues:")
	for i in range(len(zeros)):
		print("\t{:-10.5f}".format(zeros[i]), end='')
	print()
