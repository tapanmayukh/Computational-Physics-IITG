def fun_f(x, y):
	return x * x + 1.0


def runge_kutta(x0, y0, x, h):
	n = int((x - x0) / h)
	
	y = y0
	with open("data_1.dat", "w") as f:
		f.write("{} {}\n".format(x0, y))
		for i in range(1, n + 1):
			k1 = h * fun_f(x0, y)
			k2 = h * fun_f(x0 + h / 2.0, y + k1 / 2.0)
			k3 = h * fun_f(x0 + h / 2.0, y + k2 / 2.0)
			k4 = h * fun_f(x0 + h, y + k3)
			
			y = y + (1.0 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
			x0 = x0 + h
			
			f.write("{} {}\n".format(x0, y))
			
	return y


if __name__ == "__main__":
	x0 = float(input("Enter initial value for x: "))
	y0 = float(input("Enter initial value for y: "))
	x  = float(input("Enter final   value for x: "))
	h  = float(input("Enter width   value for h: "))
	
	print("\nValue of ODE at x = {} : {:-5.3f}".format(x, runge_kutta(x0, y0, x, h)))
