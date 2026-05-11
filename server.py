import socket
import threading
from router import Router
from http_request import HTTPRequest

class Server():
    def __init__(self, file_dir):
        self.file_dir = file_dir

        self.server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
        self.server_socket.listen()

    def start(self):
        try:
            while True:

                #Wait for a connection
                print("Waiting for connection...")
                client_socket, addr = self.server_socket.accept()

                threading.Thread(target=self.client_thread,args=(client_socket, addr, self.file_dir)).start()

        except KeyboardInterrupt:
            print("\nServer is shutting down")
        finally:

            #Clean up the server socket
            self.server_socket.close()
            print("\nServer has been shut down")
    
    def client_thread(self, client_socket, addr, file_dir = None):
        print(f"Connection from {addr} has been established.")

        r = client_socket.recv(1024)
        decoded_r = r.decode()

        http_req = HTTPRequest(raw = decoded_r)
        res = Router().route(self.file_dir, http_req)

        res.send(client_socket)