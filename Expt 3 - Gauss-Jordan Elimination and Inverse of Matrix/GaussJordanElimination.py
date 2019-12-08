# Solve system of linear equations using Gauss-Jordan Elimination.

# Tapan Mayukh - 170121048 - 19/08/2019


def sort_by_zeros(A, b):
	n = len(A)

	zeros = [0 for i in range(n)]
	for i in range(n):
		for j in range(len(A[0])):
			if A[i][j] != 0:
				break
			zeros[i] += 1

	for i in range(n):
		if max(zeros) <= 0:
			break
		max_idx = zeros.index(max(zeros))
		
		if max_idx != n-i-1:
			print("Swap Row {} with Row {}".format(n - i, max_idx + 1))
		
		A[max_idx], A[n-i-1] = A[n-i-1], A[max_idx]
		b[max_idx], b[n-i-1] = b[n-i-1], b[max_idx]
		
		zeros[max_idx] = -1
		zeros[n-i-1], zeros[max_idx] = zeros[max_idx], zeros[n-i-1]


def gauss_jordan(A, b):
	assert(len(A) == len(A[0]))
	assert(len(A) == len(b))
	
	n = len(A)
	A = A[:]
	b = b[:]
	
	for i in range(n):
		sort_by_zeros(A, b)
		one = i
		
		for j in range(i + 1, n):
			if A[i][i] == 0 and A[j][i] != 0:
				one = j
			if abs(A[j][i]) == 1:
				one = j
		
		if one != i:
			print("Swap Row {} with Row {}".format(one + 1, i + 1))
			A[i], A[one] = A[one], A[i]
			b[i], b[one] = b[one], b[i]
		
		for j in range(0, n):
			if j == i:
				continue
			t = A[j][i] / A[i][i]
			
			print("Row {} -= {} * Row {}".format(j + 1, t, i + 1))
			
			for k in range(i, n):
				A[j][k] -= t * A[i][k]
			
			b[j][0] -= t * b[i][0]
		
			print()
			for l in range(n):
				for k in range(n):
					print('{:-7.2f}'.format(A[l][k]), end=' ')
				print('|| {:-7.2f}\n'.format(b[l][0]), end='')
			print()
		
		print("Row{} /= {}".format(i + 1, A[i][i]))
		
		t = A[i][i]
		b[i][0] /= t
		for j in range(n):
			A[i][j] /= t
			
		print()
		for l in range(n):
			for k in range(n):
				print('{:-7.2f}'.format(A[l][k]), end=' ')
			print('|| {:-7.2f}\n'.format(b[l][0]), end='')
		print()
		
	return A, b


if __name__ == "__main__":
	A = []
	b = []
	
	n = int(input("Enter the number of equations: "))
	for i in range(n):
		var = list(map(int, input("Enter Row {} of coefficient matrix: ".format(i+1)).split()))
		A.append(var)
	for i in range(n):
		var = list(map(int, input("Enter Row {} of constant vector: ".format(i+1)).split()))
		b.append(var)
	I, ans = gauss_jordan(A, b)
	
	print("Answer:\n")
	for k in range(len(ans)):
		print('{:-7.2f}'.format(ans[k][0]), end=' ')
	print()
