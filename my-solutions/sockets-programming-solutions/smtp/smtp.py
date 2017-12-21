import base64
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver =  'smtp.163.com' # Fill in start   #Fill in end
username = 'your_username@163.com'
password = 'your_password'
sender = username
recipient = username
# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
# Fill in end
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'220':
    print('220 reply not received from server.')
    exit(0)

# Send HELO command and print server response.
heloCommand = b'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'250':
    print('250 reply not received from server.')
    exit(0)

# Apply login
clientSocket.send(b'AUTH LOGIN\r\n')
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'334':
    print('334 reply not received from server.')
    exit(0)

# Login username
clientSocket.send(base64.b64encode(bytes(username, 'ascii')) + b'\r\n')
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'334':
    print('334 reply not received from server.')
    exit(0)

# Login password
clientSocket.send(base64.b64encode(bytes(password, 'ascii')) + b'\r\n')
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'235':
    print('235 reply not received from server.')
    exit(0)

# Send MAIL FROM command and print server response.
# Fill in start
clientSocket.send(b'MAIL FROM: <' + bytes(sender, 'ascii') + b'>\r\n')
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'250':
    print('250 reply not received from server.')
    exit(0)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
clientSocket.send(b'RCPT TO: <'+ bytes(recipient, 'ascii') + b'>\r\n')
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'250':
    print('250 reply not received from server.')
    exit(0)
# Fill in end

# Send DATA command and print server response.
# Fill in start
clientSocket.send(b'DATA\r\n')
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'354':
    print('354 reply not received from server.')
    exit(0)
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(b'Subject: test message\r\n')
clientSocket.send(b'From:""< ' + bytes(sender, 'ascii') + b'>\r\n')
clientSocket.send(b'To:""< ' + bytes(recipient, 'ascii') + b'>\r\n')

clientSocket.send(bytes(msg, encoding='ascii'))
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(bytes(endmsg, encoding='ascii'))
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'250':
    print('250 reply not received from server.')
    exit(0)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send(b'QUIT\r\n')
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'221':
    print('250 reply not received from server.')
    exit(0)
# Fill in end
