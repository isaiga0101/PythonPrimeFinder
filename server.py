import socket
import time
import threading

class client_thread(threading.Thread):
        def __init__(self,threadSocket, Address):
                threading.Thread.__init__(self)
                self.threadSocket = threadSocket
                self.Address = Address
                
        def run(self):
                print('New thread created for connection to '+str(self.Address))
                while True:
                        data = self.threadSocket.recv(1024).decode()
                        if not data:
                                break
                        print ("From connected user: " + str(data))

                        data = input("Response: ")
                        if data == 'q':
                                break
                        self.threadSocket.send(data.encode())
                
                print('Connection closed to client'+ str(self.Address))
                self.threadSocket.close()
	
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('', 0))
print ('Server is at: '+ socket.gethostname()+ ':' + str(mySocket.getsockname()[1]))
	
mySocket.listen(5)
while 1:
	#accept connections from outside
	(clientsocket, address) = mySocket.accept()
	#now do something with the clientsocket
	#in this case, we'll pretend this is a threaded server
	ct = client_thread(clientsocket,address)
	ct.start()
