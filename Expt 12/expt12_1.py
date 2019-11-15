import numpy as np


def crank_nicholson(u0, b, L, tf, dt = 0.1, dx = 0.1, D = 0.2):
	m = int(np.ceil(L / dx)) - 1
	n = int(np.ceil(tf / dt))
	
	alpha = D * dt / (2 * dx * dx)
	
	A = np.zeros((m, m))
	B = np.zeros((m, m))
	
	for i in range(m):
		for j in range(m):
			if i == j:
				A[i][j] = 1 + 2 * alpha
				B[i][j] = 1 - 2 * alpha
			elif abs(i - j) == 1:
				A[i][j] = -alpha
				B[i][j] = alpha
	
	b = 2 * alpha * b
	
	u_evol = []
	u_evol.append(u0)
	
	u = np.zeros_like(u0)
	for i in range(n):
		AA = A
		BB = B @ u0 + b
		u = np.linalg.solve(AA, BB)
		
		u0 = u
		u_evol.append(u0)
	
	return u_evol


if __name__ == "__main__":
	L = 1.2
	tf = 50
	
	dx = 0.1
	dt = 0.1
	
	m = int(np.ceil(L / dx)) - 1
	
	u0 = np.zeros((m, 1))
	x = np.linspace(0, L, m + 2)
	
	for i in range(m):
		u0[i] = x[i+1] * (L - x[i + 1])
	
	b = np.zeros_like(u0)
	b[0] = 0
	b[-1] = 0
	
	u_evol = crank_nicholson(u0, b, L, tf, dt, dx)
	
	with open("data1.dat", "w") as f:
		for i in range(len(x)):
			if i == 0:
				f.write("{} {} {} {}\n".format(x[i], b[i][0], b[i][0], b[i][0]))
			elif i == len(x) - 1:
				f.write("{} {} {} {}\n".format(x[i], b[-1][0], b[-1][0], b[-1][0]))
			else:
				f.write("{} {} {} {}\n".format(x[i], u_evol[10][i - 1][0], u_evol[20][i - 1][0], u_evol[100][i - 1][0]))

#	with open("data1.dat", "w") as f:
#		t = 0
#		while t < len(u_evol):
#			for i in range(len(x)):
#				if i == 0:
#					f.write("{} {} {}\n".format(x[i], t * dt, b[i][0]))
#				elif i == len(x) - 1:
#					f.write("{} {} {}\n".format(x[i], t * dt, b[-1][0]))
#				else:
#					f.write("{} {} {}\n".format(x[i], t * dt, u_evol[t][i - 1][0]))
#			
#			t += 1
