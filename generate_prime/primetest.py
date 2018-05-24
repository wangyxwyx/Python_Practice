import math
import time

def getprimenumber(n):
	if(n==1):
		return 2
	primelst = [2]
	num  = 3
	while(len(primelst)<n):
		index =0
		isprime = True
		while(primelst[index]<=math.sqrt(num) and isprime == True):
			if(num % primelst[index] == 0):
				isprime = False
			index += 1				
		if(isprime == True):
			primelst.append(num)
		num += 1
	return num-1
	
start_time = time.time()
print(getprimenumber(10001))
print("----%s seconds----" % (time.time()-start_time))