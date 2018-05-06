

# This first part creates a dictionary from the file

file = open("sourcefile.txt" , "r") #open a file
d_pass={} # start an empty password dictionary named d_pass
for line in file:  #read the file line by line to fill dictionary
	x=line.split(",") #split the line into two X0 & X1 around the comma
	name=x[0] #populate the $name variable with the name from the input file
	password=x[1] #populate the $password variable with the password 
	c=len(password)-1 # count the length of the password so that we can remove \n
	password=password[0:c] #subtract a character to get rid of \n
	d_pass[name]=password #poplate the dictionary with the variables $name & $password
	

#Now to try and test the passwords
	plength=len(password) #get the length of the users passwords
	minlength=8; #set the minimum lenght of the password

	#print(plength)
	#print(minlength)
	if (plength < minlength):    
		print(name , "'s password is too short!")
	else:
		print (name, "'s password is long enough :-)")






