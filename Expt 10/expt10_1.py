from math import pi


def fun_f(x, y, z):
	return z


def fun_g(x, y, z):
	return 12.0 * y - z


def runge_kutta(x0, y0, z0, x, h):
	n = int((x - x0) / h)
	
	y = y0
	z = z0
	with open("data_{}.dat".format(z0), "w") as f:
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


def shoot(x0, y0, xn, yn, h):
#	al0 = float(input("\n\nEnter guess 1: "))
#	al1 = float(input("\n\nEnter guess 2: "))

	al0 = (yn - y0) / (xn - x0)
	al1 = 2 * (yn - y0) / (xn - x0)
	
	b0 = runge_kutta(x0, y0, al0, xn, h)
	b1 = runge_kutta(x0, y0, al1, xn, h)
	
	if abs(b0 - yn) / abs(yn) < 0.0001:
		return al0
	elif abs(b1 - yn) / abs(yn) < 0.0001:
		return al1
	
	al2 = al1 + (yn - b1) * (al1 - al0) / (b1 - b0)
	b2 = runge_kutta(x0, y0, al2, xn, h)
	
	while abs(b2 - yn) / abs(yn) > 0.0001:
		al0 = al1
		al1 = al2
	
		b0 = b1
		b1 = b2
		
		al2 = al1 + (yn - b1) * (al1 - al0) / (b1 - b0)
		b2 = runge_kutta(x0, y0, al2, xn, h)

	return al2


if __name__ == '__main__':
#	x0 = float(input("Enter the value of x0: "))
#	y0 = float(input("Enter the value of y0: "))
#	xn = float(input("Enter the value of xn: "))
#	yn = float(input("Enter the value of yn: "))

	x0 = 0.0
	y0 = -2.0
	xn = 1.0
	yn = -80.3054
	
	h = float(input("Enter the value of h : "))
	
	arr = []
	
	i = x0
	while i <= xn:
		arr.append([])
		i += h
	
	alpha = shoot(x0, y0, xn, yn, h)
	
	x = 2.0
	
#	h = -0.1
	val = runge_kutta(x0, y0, alpha, x, h)
	
	print("Thus, correct value of alpha to convert the BVP in IVP: {}".format(alpha))
	print("\nThe value of function at x = {}: {}".format(x, val))
