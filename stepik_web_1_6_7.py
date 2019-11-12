import socket
import os       

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(5)
while True:
    client = 1
    sclient, addr = s.accept()
    child_pid = os.fork()
    if child_pid == 0: 
        while True:
            data = soc.recv(1024)
            if not data or data == 'close':
                break
            sclient.send(data)
            print(sclient, client, data, 'OK')
        sclient.close()
            client += 1     
