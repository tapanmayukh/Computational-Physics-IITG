from random import random

class Matrix:
	'''
	Defines a matrix class.
	'''
	def __init__(self, r = 2, c = 2):
		'''
		Initialize a matrix with given rows and cols and random values.
		'''
		self.row = r
		self.col = c
		
		self.matrix = []
		
		for i in range(r):
			self.matrix.append([])
			for j in range(c):
				self.matrix[i].append(random() * 2 - 1)
	
	
	@staticmethod
	def from2DArray(arr):
		'''
		Initialize a matrix with given 2D Array.
		'''
		matrix = Matrix(len(arr), len(arr[0]))
		for i in range(len(arr)):
			for j in range(len(arr[0])):
				matrix.matrix[i][j] = arr[i][j]
		
		return matrix


	@staticmethod
	def from1DArray(arr, r, c):
		'''
		Initialize a matrix with given 1D Array.
		'''
		if len(arr) != r * c:
			raise IndexError("Number of element doesn't matrixch.")

		matrix = Matrix(r, c)
		for i in range(r):
			for j in range(c):
				matrix.matrix[i][j] = arr[i * c + j]
		
		return matrix
	
	
	def transpose(self, inplace = False):
		'''
		Find the transpose of given matrix.
		'''
		matrix = Matrix(self.col, self.row)
		
		for i in range(self.row):
			for j in range(self.col):
				matrix.matrix[j][i] = self.matrix[i][j]
		
		if inplace:
			del self
			self = matrix
		
		return matrix
	
	
	def del_matrix(self, r, c):
		'''
		Create a new matrix by deleting given row and col.
		'''
		matrix = Matrix(self.row - 1, self.col - 1)
		
		for i in range(self.row):
			for j in range(self.col):
				if i < r and j < c:
					matrix.matrix[i][j] = self.matrix[i][j]
				elif i < r and j > c:
					matrix.matrix[i][j - 1] = self.matrix[i][j]
				elif i > r and j < c:
					matrix.matrix[i - 1][j] = self.matrix[i][j]
				elif i > r and j > c:
					matrix.matrix[i - 1][j - 1] = self.matrix[i][j]
		
		return matrix
	
	
	def determinant(self):
		'''
		Find the determinant of given matrix.
		'''
		if self.row != self.col:
			raise IndexError("Not a Square matrix.")
		
		elif self.row == 1:
			return self.matrix[0][0]
		elif self.row == 2:
			return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
		
		det = 0
		
		for i in range(self.col):
			det += pow(-1, i) * self.matrix[0][i] * self.del_matrix(0, i).determinant()
		
		return det
	
	def display(self):
		for i in range(self.row):
			print(self.matrix[i])



if __name__ == "__main__":
	r = int(input("Enter number of rows: "))
	c = int(input("Enter number of cols: "))
	
	arr = list(map(int, input("Enter the matrix elements in sequence (row-wise, space-separated):\n").split()))
	
	matrix = Matrix.from1DArray(arr, r, c)
	
	print("\nOriginal matrix:\n")
	matrix.display()
	
	matrix_T = matrix.transpose()
	print("\nTransposed matrix:\n")
	matrix_T.display()
	
	print("\nDeterminant of Original matrix: {}".format(matrix.determinant()))
	print("Determinant of Transposed matrix: {}".format(matrix_T.determinant()))
