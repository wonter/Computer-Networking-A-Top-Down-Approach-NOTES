# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverSocket.bind(('', 7888))
serverSocket.listen()
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() # Fill in start  #Fill in end
    try:
        message = str(connectionSocket.recv(4096), encoding='utf-8') # Fill in start  # Fill in end
        if not message:
            connectionSocket.close()
            continue

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() # Fill in start  #Fill in end
        # 这里是解决一下windows下中文乱码问题
        outputdata_bytes = bytes(outputdata, encoding='gb18030')

        # Send one HTTP header line into socket
        # Fill in start
        headers = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\nContent-Length: {}\n\n'.format(len(outputdata_bytes))
        connectionSocket.send(bytes(headers, encoding='utf-8'))
        # Fill in end

        # Send the content of the requested file to the client
        connectionSocket.send(outputdata_bytes)
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        outputdata_bytes = bytes('Not Found', encoding='utf-8')
        headers = 'HTTP/1.1 404 Not Found\nContent-Type: text/html; charset=utf-8\nContent-Length: {}\n\n'.format(len(outputdata_bytes))
        connectionSocket.send(bytes(headers, encoding='utf-8'))
        connectionSocket.send(outputdata_bytes)
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
serverSocket.close()