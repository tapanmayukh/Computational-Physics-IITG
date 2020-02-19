# Numerical Solution to Simple Harmonic Motion using Taylor's Expansion
# d2x / dt2 = -(k / m) * x

# Tapan Mayukh - 170121048 - 30/09/2019

from math import sqrt

x0 = float(input("Enter starting position: "))
v0 = float(input("Enter starting velocity: "))
k = float(input("Enter spring constant: "))
m = float(input("Enter mass of the pendulum: "))

h = pow(10, -5)

x1 = x0 + v0 * h
w = sqrt(k / m)

t = 10
n = int(t / h)

f1 = open("data.dat", "w")

for i in range(n + 1):
	if i == 0:
		f1.write("{} {}\n".format(i * h, x0))
	elif i == 0:
		f1.write("{} {}\n".format(i * h, x1))
	else:
		x2 = (2.0 - (h * h) * (w * w)) * x1 - x0
		x0 = x1
		x1 = x2
		f1.write("{} {}\n".format(i * h, x2))
