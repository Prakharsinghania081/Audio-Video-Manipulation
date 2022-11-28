import numpy

n = 20
a = numpy.empty(n)

for i in range(n):
	a[i] = 100+i

print(f"a={a}")

b = a[::2]
print(b)

c = a[1::2]
print(c)

d = a[::-1]
print(d)

e = a[::-2]
print(e)

f = numpy.empty(a.size)
f[::2] = a[1::2]
f[1::2] = a[::2]
print(f)

g = a[::2] + a[1::2]
g = g/2
print(g)

