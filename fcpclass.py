from images_fcp import *

def findColour(x0, y0):
	x, y = 0, 0
	count = 0
	maxCount = 20

	while( x*x + y*y < 4 and count < maxCount ):
		t = x*x - y*y + x0
		y = 2*x*y + y0
		x = t
		count = count + 1

	if count < maxCount:
		return ( 255*count/20 , count*count%256, 0)

	return (255, 255, 255)

#=======================================================
w = 501
h = 501

b = [ [ (0,0,0) for col in range(w) ] for row in range(h) ]

# x = -2.00 to 0.50 => 2.5 units wide
# y = -1.25 to 1.25 => 2.5 units tall

for row in range(h):
	for col in range(w):
		x = -2.00 + col*2.5/500
		y = -1.25 + row*2.5/500

		b[row][col] = findColour(x,y)

writeImage(b, "outx.jpg")

