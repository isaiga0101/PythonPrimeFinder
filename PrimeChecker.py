import sys

# Calculates a percentage 
def percent(num,total):
	holder = num/total
	holder = holder * 100
	return holder
	
#This handles checking if a number is prime	
def isprime(n):
	progress = 0
	TempPr = 0
	printprogress = 0
	'''check if integer n is a prime'''

	# make sure n is a positive integer
	n = abs(int(n))
	print ("Initializing")

	# 0 and 1 are not primes
	if n < 2:
		return False

	# 2 is the only even prime number
	if n == 2: 
		return True    

	# all other even numbers are not primes
	if not n & 1: 
		return False

	# range starts with 3 and only needs to go up 
	# the square root of n for all odd numbers
	print("0 %")
	for x in range(3, int(n**0.5) + 1, 2):
		if n % x == 0:
			return False
			
		progress = percent(x,int(n**0.5))
		if progress >= TempPr + 1:
			printprogress = printprogress + 1
			sys.stdout.write('\r'+b)
			print(printprogress, '%') 
			TempPr = TempPr + 1
	return True

# This handles console IO

print("Prime Checker")
print("programed by: Isaiah Gayfield")
print("Start Date: 7/20/2016")
print("Version: 0.1.0")

while 1:
	#Initialize variable if there is no input.
	primeCk = 0
	
	print("Input a number to check for primality and press \"Enter\" Enter \"Exit\" to exit.")
	primeCk = input(">> ")
	
	if primeCk == "exit":
		sys.exit()
	elif primeCk == "Exit":
		sys.exit()
	
	primeCk = int(primeCk)
	primebool = isprime(primeCk)
	if primebool == True:
		print(primeCk,'is prime')
		
	elif primebool == False:
		print(primeCk,'is not prime')
