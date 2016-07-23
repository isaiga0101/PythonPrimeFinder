#This handles checking if a number is prime
def isprime(n):

	'''check if integer n is a prime'''

	# make sure n is a positive integer
	n = abs(int(n))

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
	for x in range(3, int(n**0.5) + 1, 2):
		if n % x == 0:
			return False

	return True

# This handles console IO

print("Prime Checker")
print("programed by: Isaiah Gayfield")
print("Start Date: 7/20/2016")
print("Version: 0.0.0")

while 1:
	#Initialize variable if there is no input.
	primeCk = 0
	
	print("Input a number to check for primality and press Enter")
	primeCk = input(">> ")
	if isprime(primeCk) == True:
		print('%d is prime', primeCk)
		
	elif isprime(primeCk) == False:
		print('%d is not prime', primeCk)
