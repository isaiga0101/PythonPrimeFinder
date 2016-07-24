import socket
 
def Main():
	host = input('Host: ')
	port = int(input('Port: '))
	print('Connecting to: '+host+':'+str(port))
	mySocket = socket.socket()
	mySocket.connect((host,port))
		
	message = input("Message: ")
		
	while message != 'q':
		mySocket.send(message.encode())
		data = mySocket.recv(1024).decode()
		
		print ('Received from server: ' + data)
		
		message = input("Message: ")
				
	mySocket.close()
 
if __name__ == '__main__':
	Main()
