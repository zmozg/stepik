import socket

def server_receive(sock, msglen):
    msg = ''
    while len(msg) < msglen:
        chunk = sock.recv(msglen-len(msg))
        if chunk == '':
            sclient.close()
            raise RuntimeError('br')
        msg += chunk
    return msg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

while True:
    sclient, addr = s.accept()
    while True:
        data = server_receive(sclient, 1024)
        if not data:
            break
        if data == 'close':
            sclient.close()
        conn.send(data)
    
