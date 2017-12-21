import time
from socket import *

socket = socket(AF_INET, SOCK_DGRAM)
socket.settimeout(1)

for seq in range(10):
    send_time = time.time()
    msg = 'Ping {} {}'.format(seq, send_time)
    socket.sendto(bytes(msg, encoding='utf-8'), ('localhost', 12000))
    try:
        msg, address = socket.recvfrom(4096)
    except timeout:
        print('Time out')
    else:
        recv_time = time.time()
        print('Seq{}: RTT {:.4f}s'.format(seq, recv_time - send_time))
