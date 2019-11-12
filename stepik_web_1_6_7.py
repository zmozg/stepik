import socket
import os

def handle_client(soc):
    while True:
        data = soc.recv(1024)
        if not data or data == 'close':
            break
        soc.send(data)
    soc.close()

            

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(5)
while True:
   client = 1
   while client <= 10:
       sclient, addr = s.accept()
       child_pid = os.fork()
       if child_pid == 0:
           handle_client(sclient)
       else:
           client += 1


