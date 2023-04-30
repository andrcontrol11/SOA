import os
import socket
import socketserver
import json

#https://docs.python.org/3/library/socketserver.html

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket1 = self.request[1]
        print(data.decode())
        data_dict = json.loads(data.decode())
        print(data_dict)
        host = data_dict["format"]
        port = int(os.environ['PORT'])
        socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket2.sendto(bytes("", "utf-8"), (host, port))
        response = socket2.recv(1024)
        socket1.sendto(response, self.client_address)
        socket2.close()


if __name__ == "__main__":
    with socketserver.UDPServer(("0.0.0.0", 2000), MyUDPHandler) as server:
        print("CLIENT1")
        server.serve_forever()