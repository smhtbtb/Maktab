import socket
import translators as ts

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b'Hello, world')
    a = ts.google('hello world', to_language='fa')
    s.sendall(b'a')

    data = s.recv(1024)

print('Received', repr(data))

