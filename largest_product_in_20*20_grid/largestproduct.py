import numpy as np

def switchprod(x,y):
	if(y>x):
		return y
	return x

def south(a, i, j):
	return a.item(i,j)*a.item(i,j+1)*a.item(i,j+2)*a.item(i,j+3)

def east(a, i, j):
	return a.item(i,j)*a.item(i+1,j)*a.item(i+2,j)*a.item(i+3,j)

def southeast(a, i, j):
	return a.item(i,j)*a.item(i+1,j+1)*a.item(i+2,j+2)*a.item(i+3,j+3)

def northeast(a, i, j):
	return a.item(i,j)*a.item(i+1,j-1)*a.item(i+2,j-2)*a.item(i+3,j-3)

def largestproduct(a):
	prod = 0
	for i in range(0,19):
		for j in range(0,19):
			if j<=16:
				prod = switchprod(prod, south(a, i, j))
			if i<=16:
				prod = switchprod(prod, east(a, i, j))
			if i<=16 and j<=16:
				prod = switchprod(prod, southeast(a, i, j))
			if i<=16 and j>=3:
				prod = switchprod(prod, northeast(a, i, j))
	return prod

mat = np.loadtxt('matrix1.txt')
print(largestproduct(mat))