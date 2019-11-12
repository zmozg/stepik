import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
child_pid = os.fork()
if child_pid == 0:
    while True:
        sclient, addr = s.accept()
        data = sclient.recv(1024)
        sclient.send(data)
