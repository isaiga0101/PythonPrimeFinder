import socket
import time
import threading
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
			print(printprogress, '%')
			TempPr = TempPr + 1
	return True

class client_thread(threading.Thread):
        def __init__(self,threadSocket, Address,intPrime,top,bottom):
                threading.Thread.__init__(self)
                self.threadSocket = threadSocket
                self.Address = Address
                self.intPrime = intPrime
                self.top = top
                self.bottom = bottom

        def run(self):
                errorCnt = 0
                print('New thread created for connection to ' + str(self.Address))
                while True:
                        while errorCnt <= 4:
                                data = self.threadSocket.recv(1024).decode()
                                if not data:
                                        break
                                while True:
                                        # Send Prime Number
                                        if data == 'r':
                                                data = self.threadSocket.recv(1024).decode()
                                        if str(data).upper() == "RECEIVE NUMBER":
                                                data = str(self.intPrime)
                                                self.threadSocket.send(data.encode())
                                                errorCnt = 0
                                                break
                                        else:
                                                data = "resend"
                                                self.threadSocket.send(data.encode())
                                                errorCnt = errorCnt + 1
                                                data = 'r'
                                while True:
                                        data = self.threadSocket.recv(1024).decode()
                                        if not data:
                                                break
                                        # Send top num to check
                                        if data == 'r':
                                                data = self.threadSocket.recv(1024).decode()
                                        if str(data).upper() == "RECEIVE TOP":
                                                data = str(self.top)
                                                self.threadSocket.send(data.encode())
                                                errorCnt = 0
                                                break
                                        else:
                                                data = "resend"
                                                self.threadSocket.send(data.encode())
                                                errorCnt = errorCnt + 1
                                                data = 'r'

                                while True:
                                        data = self.threadSocket.recv(1024).decode()
                                        if not data:
                                                break
                                        # Send low num to check
                                        if data == 'r':
                                                data = self.threadSocket.recv(1024).decode()
                                        if str(data).upper() == "RECEIVE LOW":
                                                data = str(self.bottom)
                                                self.threadSocket.send(data.encode())
                                                errorCnt = 0
                                                break
                                        else:
                                                data = "resend"
                                                self.threadSocket.send(data.encode())
                                                errorCnt = errorCnt + 1
                                                data = 'r'
                                break
                        break
                data = self.threadSocket.recv(1024).decode()
                while True:
                        if not data:
                                break
                        # Check if client sent true or false
                        global clientCk
                        if data.upper() == 'TRUE' and clientCk != -1:
                                global clientCk
                                clientCk = clientCk + 1
                                clientDone = clientDone + 1
                                break
                        else:
                                global clientCk
                                clientCk = -1
                                global clientDone
                                clientDone = clientDone + 1
                                break

                print('Connection closed to client' + str(self.Address))
                self.threadSocket.close()

#Main --------------------------------------------------------------------------------------
print("Prime Checker")
print("programed by: Isaiah Gayfield")
print("Start Date: 7/20/2016")
print("Version: 0.1.0")
while True:
        clientDone = 0
        low = 0
        high = 0
        global clientCk
        clientCk = 0
        check = input('Enter \'Exit\' to exit, otherwise input number: ')
        if check.upper() == 'EXIT':
                break
        print('Do you want to check this with multiple computers connected wirelessly?')
        print('This is only recomended for large numbers, the default answer is no.')
        multiple = input('(y,N) :')

        if multiple == 'y':
                num = int(input('How many clients will be computing the number?: '))
                high = int(check)**0.5 / num
                if round(high,0) > high:
                        high = round(high, 0)
                else:
                        high = round(high,0) + 1
                add = high

                mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                mySocket.bind(('', 0))
                print ('Server is at: '+ socket.gethostname()+ ':' + str(mySocket.getsockname()[1]))

                mySocket.listen(num)
                while True:
                        #Accept connections from outside
                        (clientsocket, address) = mySocket.accept()
                        #Start a thead for the client socket
                        ct = client_thread(clientsocket,address,check,high,low)
                        ct.start()

                        if high == check:
                                break
                        else:
                                low = low + add
                                high = high + add
                global clientCk
                while clientCk <= num:
                        if num < 0:
                                print(str(check)+" is not prime.")
                                break
                if num >= 0:
                        print(str(check)+' is prime')

        else:
                # This handles console IO
                # Initialize variable if there is no input.
                primeCk = int(check)
                primebool = isprime(primeCk)
                if primebool == True:
                        print(primeCk,'is prime')

                elif primebool == False:
                        print(primeCk,'is not prime')
