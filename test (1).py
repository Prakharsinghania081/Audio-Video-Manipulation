from images_fcp import *

def manipulate(p): # this is (R, G, B)
	return (p[0], 0, 0)

a = readImage("udon.jpg")
w, h = len(a[0]), len(a)

b = [ [ manipulate(a[row][col]) for col in range(w) ] for row in range(h) ]


#b = [[a[h-1-j][i] for j in range(h)] for i in range(w)]

writeImage(b, "blah.jpg")

