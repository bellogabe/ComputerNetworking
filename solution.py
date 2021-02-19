#
# Gabriel Bello, programming assignment 2 - Web Server in Python
# Submitted 2/19/2021
#


#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a server socket
    #Fill in start
    serverSocket.bind(("127.0.0.1",port))
    serverSocket.listen(5)
    #print("The web server is listening on port: ",port)
    #Fill in end

    while True:
        #Establish the connection
        #print("Ready to serve...")
        connectionSocket, addr=serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
 
            #Send one HTTP header line into socket
            #Fill in start
            connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
            #Fill in end

            #Send the content of the requested file to the client
            connectionSocket.sendall(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
            
        except IOError:
            #Send response message for file not found (404)
            #Fill in start
            connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
            connectionSocket.send(b"<html><head></head><body>404 not found</body></html>")
            #Fill in end

            #Close client socket
            #Fill in start
            connectionSocket.close()
            pass
            #Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)


