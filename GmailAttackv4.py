from sys import stderr
import os
import socket
import ssl
import threading

upstream = ('127.0.0.1', 993)

# unbuffered stdout
stdout = os.fdopen(1, 'w', 0)

# log
stderr.write('incoming connection from (%r,%s)\n' % (
    os.environ['SOCAT_PEERADDR'],
    os.environ['SOCAT_PEERPORT'],
))

# connect to upstream server
server = ssl.wrap_socket(socket.create_connection(upstream))
server.sendall('0 ID ("AGUID" "A")\r\n')


# server -> client
def thread_proc():
    while 1:
        stdout.write(server.recv(1024) or os._exit(0))


thread = threading.Thread(target=thread_proc)
thread.daemon = True
thread.start()

# client -> server
while 1:
    server.sendall(os.read(0, 1024) or exit())
