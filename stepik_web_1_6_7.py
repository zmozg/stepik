import socket
import os

def hendle_client(soc):
    while True:
        data = soc.recv(1024)
        if not data or data == 'close':
            break
        soc.send(data)
    soc.close()
    return

def server(s):
   client = 1
   while client <= 10:
       sclient, addr = s.accept()
       child_pid = os.fork()
           if child_pid == 0:
               hendel_client(sclient)
           else:
               client += 1
               

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(5)

server(s)
