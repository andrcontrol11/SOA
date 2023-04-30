import os
import socket
import socketserver
import json

#https://docs.python.org/3/library/socketserver.html

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket1 = self.request[1]
        print("CLIENT3")
        print(data.decode())
        data = (data.decode()).split()
        host = data[1].upper()
        port = int(os.environ['PORT'])
        print(host, port)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket2:
            socket2.connect((host, port))
            socket2.sendto(str.encode(""), (host, port))
            response, server = socket2.recvfrom(1024)
            socket1.sendto(response, self.client_address)
            socket2.close()


if __name__ == "__main__":
    print("CLIENT1")
    with socketserver.UDPServer(("0.0.0.0", 2000), MyUDPHandler) as server:
        print("CLIENT2")
        server.serve_forever()