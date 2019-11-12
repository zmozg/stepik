import socket

def server_receive(sock, msglen):
    msg = ''
    while len(msg) < msglen:
        chunk = sock.recv(msglen-len(msg))
        if chuck = '':
            raise RuntimeError('br')
        msg += chunk
    return msg

s = socket.socket(socket.AF_INET, socet.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

while True:
    sclient, addr = s.accept()
    while True:
        data = server_receive(sclient, 1024)
        if not data:
            break
        conn.send(data)
    if data == 'close':
        sclient.close()
