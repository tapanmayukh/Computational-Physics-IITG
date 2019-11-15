def sort_by_zeros(A, I):
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
		I[max_idx], I[n-i-1] = I[n-i-1], I[max_idx]
		
		zeros[max_idx] = -1
		zeros[n-i-1], zeros[max_idx] = zeros[max_idx], zeros[n-i-1]


def inverse(A):
	assert(len(A) == len(A[0]))
	
	n = len(A)
	A = A[:]
	
	I = [[0 for i in range(n)] for i in range(n)]
	for i in range(n):
		I[i][i] = 1
	
	for i in range(n):
		sort_by_zeros(A, I)
		one = i
		
		for j in range(i + 1, n):
			if A[i][i] == 0 and A[j][i] != 0:
				one = j
			if abs(A[j][i]) == 1:
				one = j
		
		if one != i:
			print("Swap Row {} with Row {}".format(one + 1, i + 1))
			A[i], A[one] = A[one], A[i]
			I[i], I[one] = I[one], I[i]
		
		for j in range(0, n):
			if j == i:
				continue
			t = A[j][i] / A[i][i]
			
			print("Row {} -= {} * Row {}".format(j + 1, t, i + 1))
			
			for k in range(0, n):
				A[j][k] -= t * A[i][k]
				I[j][k] -= t * I[i][k]
		
			print()
			for l in range(n):
				for k in range(n):
					print('{:-7.2f}'.format(A[l][k]), end=' ')
				print("||", end='')
				for k in range(n):
					print('{:-7.2f}'.format(I[l][k]), end=' ')
				print('\n', end='')
			print()
		
		print("Row{} /= {}".format(i + 1, A[i][i]))
		
		t = A[i][i]
		for j in range(n):
			I[i][j] /= t
			A[i][j] /= t
		
		print()
		for l in range(n):
			for k in range(n):
				print('{:-7.2f}'.format(A[l][k]), end=' ')
			print("||", end='')
			for k in range(n):
				print('{:-7.2f}'.format(I[l][k]), end=' ')
			print('\n', end='')
		print()
		
	return A, I


if __name__ == "__main__":
	A = []
	
	n = int(input("Enter the number of rows: "))
	for i in range(n):
		var = list(map(int, input("Enter Row {} of matrix: ".format(i+1)).split()))
		A.append(var)
	I, A_inv = inverse(A)
