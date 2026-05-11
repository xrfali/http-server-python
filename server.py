import sys
import socket
import threading

class Server():
    def __init__(self, file_dir):
        args = sys.argv
        self.file_path = None
        self.file_dir = file_dir

        if len(args) > 2:
            self.file_path = args[2]

        self.server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
        self.server_socket.listen()

    def start(self):
        try:
            while True:

                #Wait for a connection
                print("Waiting for connection...")
                client_socket, addr = self.server_socket.accept()

                threading.Thread(target=self.client_thread,args=(client_socket, addr, self.file_path)).start()

        except KeyboardInterrupt:
            print("\nServer is shutting down")
        finally:

            #Clean up the server socket
            self.server_socket.close()
            print("\nServer has been shut down")
    
    def client_thread(self, client_socket, addr, file_dir = None):
        print(f"Connection from {addr} has been established.")

        #Handles the client request