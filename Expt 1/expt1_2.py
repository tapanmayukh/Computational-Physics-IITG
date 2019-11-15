from math import sin, cos, exp, pi


def fact(n):
	if n == 0 or n == 1:
		return 1
	
	return n * fact(n - 1)


angle = float(input("Enter the angle (in degrees): "))
rad = angle * pi / 180


# sin-function values
a1 = sin(rad)
print("\nsin-function:")
print("By sin({}): {}\n".format(angle, a1))

a2 = 0
err = 100
n = 0

## 0.1% Error Part
print("0.1% part:\n")
while err > 0.1:
	a2 += pow(-1, n) * pow(rad, 2 * n + 1) / fact(2 * n + 1)
	err = abs(a1 - a2) * 100 / abs(a1)
	n += 1

print("By expansion: {}".format(a2))
print("Final Error: {}".format(err))
print("Number of terms: {}".format(n))

a2 = 0
err = 100
n = 0

## 1% Error Part
print("\n1% part:\n")
while err > 1:
	a2 += pow(-1, n) * pow(rad, 2 * n + 1) / fact(2 * n + 1)
	err = abs(a1 - a2) * 100 / abs(a1)
	n += 1

print("By expansion: {}".format(a2))
print("Final Error: {}".format(err))
print("Number of terms: {}".format(n))


# cos-function values
a1 = cos(rad)
print("\ncos-function:")
print("By cos({}): {}\n".format(angle, a1))

a2 = 0
err = 100
n = 0

## 0.1% Error Part
print("0.1% part:\n")
while err > 0.1:
	a2 += pow(-1, n) * pow(rad, 2 * n) / fact(2 * n)
	err = abs(a1 - a2) * 100 / abs(a1)
	n += 1

print("By expansion: {}".format(a2))
print("Final Error: {}".format(err))
print("Number of terms: {}".format(n))

a2 = 0
err = 100
n = 0

## 1% Error Part
print("\n1% part:\n")
while err > 1:
	a2 += pow(-1, n) * pow(rad, 2 * n) / fact(2 * n)
	err = abs(a1 - a2) * 100 / abs(a1)
	n += 1

print("By expansion: {}".format(a2))
print("Final Error: {}".format(err))
print("Number of terms: {}".format(n))

# exp-function values
a1 = exp(rad)
print("\nexp-function:")
print("By exp[({}): {}\n".format(angle, a1))

a2 = 0
err = 100
n = 0

## 0.1% Error Part
print("0.1% part:\n")
while err > 0.1:
	a2 += pow(rad, n) / fact(n)
	err = abs(a1 - a2) * 100 / abs(a1)
	n += 1

print("By expansion: {}".format(a2))
print("Final Error: {}".format(err))
print("Number of terms: {}".format(n))

a2 = 0
err = 100
n = 0

## 1% Error Part
print("\n1% part:\n")
while err > 1:
	a2 += pow(rad, n) / fact(n)
	err = abs(a1 - a2) * 100 / abs(a1)
	n += 1

print("By expansion: {}".format(a2))
print("Final Error: {}".format(err))
print("Number of terms: {}".format(n))



with open("sin_data.txt", "w") as f:
	pass

i = -3.0
while i <= 4.0:
	a1 = sin(rad)

	a2 = 0
	err = 100
	n = 0

	while err > 0.1:
		a2 += pow(-1, n) * pow(rad, 2 * n + 1) / fact(2 * n + 1)
		err = abs(a1 - a2) * 100 / abs(a1)
		n += 1
	
	with open("sin_data.txt", "a+") as f:
		f.write("{},{},{}\n".format(i, a1, a2))
	
	i += 0.05
