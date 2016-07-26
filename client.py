import socket

# Calculates a percentage
def percent(num,total):
	holder = num/total
	holder = holder * 100
	return holder

#This handles checking if a number is prime
def isprime(n,low,top):
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
	for x in range(low, top, 2):
		if n % x == 0:
			return False

		progress = percent(x,top)
		if progress >= TempPr + 1:
			printprogress = printprogress + 1
			print(printprogress, '%')
			TempPr = TempPr + 1
	return True


def Main():
	count = 1
	host = input('Host: ')
	port = int(input('Port: '))
	print('Connecting to: '+host+':'+str(port))
	mySocket = socket.socket()
	mySocket.connect((host,port))
		
	message = 'receive number'
		
	while count <= 3:
		mySocket.send(message.encode())
		data = mySocket.recv(1024).decode()
		if not data:
			break
		print ('Received from server: ' + data)
		if count == 1:
			num = int(data)
			message = 'receive top'
			count = count + 1
		if count == 2:
			top = int(data)
			message = 'receive low'
			count = count + 1
		if count == 3:
			low = int(data)
			count = count + 1

	primenum = isprime(num,top,low)
	if primenum == True:
		mySocket.send('True'.encode())
	else:
		mySocket.send('False'.encode())
	mySocket.close()
 
if __name__ == '__main__':
	Main()
