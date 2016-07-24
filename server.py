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
# Main
acceptclient = True
check = int(input('Prime to check: '))
print('Do you want to check this with multiple computers connected wirelessly?')
print('This is only recomended for large numbers, the default answer is no.')
multiple = input('(y,N) :')

if multiple == y:
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.bind(('', 0))
        print ('Server is at: '+ socket.gethostname()+ ':' + str(mySocket.getsockname()[1]))
                
        mySocket.listen(5)
        while acceptcleint == True:
                #accept connections from outside
                (clientsocket, address) = mySocket.accept()
                #Start a thead for the client socket
                ct = client_thread(clientsocket,address)
                ct.start()

else:
        
