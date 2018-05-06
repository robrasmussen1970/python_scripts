numbers = []
for i in range(1,1001): # Last digit is ignored
	if(i%4 ==0):
		numbers.append(str(i))
print ("Numbers between 1 and 1000 that are devisible by 4")
		
print (','.join(numbers))
