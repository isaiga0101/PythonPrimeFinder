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
			sys.stdout.write('\r'+b)
			print(printprogress, '%') 
			TempPr = TempPr + 1
	return True

class client_thread(threading.Thread):
        def __init__(self,threadSocket, Address,intPrime):
                threading.Thread.__init__(self)
                self.threadSocket = threadSocket
                self.Address = Address
                
        def run(self):
                print('New thread created for connection to '+str(self.Address))
                while True:
                        data = self.threadSocket.recv(1024).decode()
                        if not data:
                                break
                        if str(data) == "Receive Number":
                                #Heeeerrreeee
                                self.threadSocket.send(data.encoe())
                                
                        data = input("Response: ")
                        if data == 'q':
                                break
                        self.threadSocket.send(data.encode())
                
                print('Connection closed to client'+ str(self.Address))
                self.threadSocket.close()
                
#Main --------------------------------------------------------------------------------------                
print("Prime Checker")
print("programed by: Isaiah Gayfield")
print("Start Date: 7/20/2016")
print("Version: 0.1.0")

acceptclient = True
check = int(input('Prime to check: '))
print('Do you want to check this with multiple computers connected wirelessly?')
print('This is only recomended for large numbers, the default answer is no.')
multiple = input('(y,N) :')

if multiple == y:
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.bind(('', 0))
        print ('Server is at: '+ socket.gethostname()+ ':' + str(mySocket.getsockname()[1]))
        global clientCount
        clientCount = 0
        
        mySocket.listen(5)
        while acceptclient == True:
                #accept connections from outside
                (clientsocket, address) = mySocket.accept()
                #Start a thead for the client socket and add 1 to global client count
                clientCount = clientCount + 1
                ct = client_thread(clientsocket,address,check)
                ct.start()

else:
        # This handles console IO
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
