import socket

def server_receive(sock, msglen):
    msg = ''
    while len(msg) < msglen:
        chunk = sock.recv(msglen-len(msg))
        if chunk == '':
            raise RuntimeError('br')
        msg += chunk
    return msg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

while True:
    sclient, addr = s.accept()
    while True:
        data = sclient.recv(1024)
        if not data or data == 'close':
            break
        sclient.send(data)
    sclient.close()
    
