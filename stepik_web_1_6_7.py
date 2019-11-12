import socket
import os

def handle_client(soc, conn):
    while True:
        data = soc.recv(1024)
        if not data or data == 'close':
            break
        soc.send(data)
        print(conn)
    soc.close()

            

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(5)
while True:
   client = 1
   while client <= 10:
       child_pid = os.fork()
       if child_pid == 0:
           sclient, addr = s.accept()
           handle_client(sclient, client)
       else:
           client += 1
