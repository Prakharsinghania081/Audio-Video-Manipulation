from images_fcp import *

a = readImage("xi.jpg")
w, h = len(a[0]), len(a)

kernel1 = [
	[0, 1, 0],
	[1, -3, 1],
	[0, 1, 0]
]

b = convolve(a, kernel1)

writeImage(b, "xi2.jpg")