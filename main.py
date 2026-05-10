import socket

def process_request(client_socket):

    #Read data from client
    d = client_socket.recv(1024)

    #Send a 200 OK response
    client_socket.send(b"HTTP/1.1 200 OK\r\n\r\n")
    client_socket.close()

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.listen()
    
    try:
        while True:

            #Wait for a connection
            print("Waiting for connection...")
            client_socket, addr = server_socket.accept()

            print(f"Connection from {addr} has been established.")

            #Handles the client request
            process_request(client_socket)

    except KeyboardInterrupt:
        print("\nServer is shutting down")
    finally:

        #Clean up the server socket
        server_socket.close()
        print("\nServer has been shut down")

if __name__ == "__main__":
    main()