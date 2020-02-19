# Numerical Solution to 2nd order ODE using 4th order Runge-Kutta Method
# d2y / dx2 + dy / dx + 1 = 0

# Tapan Mayukh - 170121048 - 14/10/2019


def fun_f(x, y, z):
	return z


def fun_g(x, y, z):
	return - y - z


def runge_kutta(x0, y0, z0, x, h):
	n = int((x - x0) / h)
	
	y = y0
	z = z0
	with open("data_2.dat", "w") as f:
		f.write("{} {}\n".format(x0, y))
		for i in range(1, n + 1):
			k1 = h * fun_f(x0, y, z)
			l1 = h * fun_g(x0, y, z)
			
			k2 = h * fun_f(x0 + h / 2.0, y + k1 / 2.0, z + l1 / 2.0)
			l2 = h * fun_g(x0 + h / 2.0, y + k1 / 2.0, z + l1 / 2.0)
			
			k3 = h * fun_f(x0 + h / 2.0, y + k2 / 2.0, z + l2 / 2.0)
			l3 = h * fun_g(x0 + h / 2.0, y + k2 / 2.0, z + l2 / 2.0)
			
			k4 = h * fun_f(x0 + h, y + k3, z + l3)
			l4 = h * fun_g(x0 + h, y + k3, z + l3)
			
			z = z + (1.0 / 6) * (l1 + 2 * l2 + 2 * l3 + l4)
			y = y + (1.0 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
			x0 = x0 + h
			
			f.write("{} {}\n".format(x0, y))
			
	return y


if __name__ == "__main__":
	x0 = float(input("Enter initial value for x : "))
	y0 = float(input("Enter initial value for y : "))
	z0 = float(input("Enter initial value for y': "))
	x  = float(input("Enter final   value for x : "))
	h  = float(input("Enter width   value for h : "))
	
	print("\nValue of ODE at x = {} : {:-7.5f}".format(x, runge_kutta(x0, y0, z0, x, h)))
